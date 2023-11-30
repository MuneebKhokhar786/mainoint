from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.cache import cache
from django.db.models import Count, OuterRef, Subquery
from .models import Product, Collection, ProductImage
from .decorators import ajax_login_required

def get_first_product_image():
    return ProductImage.objects.filter(
        product=OuterRef('pk')).order_by('id')[:1]

def get_user_id():
    return cache.get('user_id')

def get_user_cart(user_id):
    return cache.get(user_id, {'cart': {}})['cart']

def get_total_quantity(cart):
    return sum(cart.values())

def get_products_with_first_image():
    products = Product.objects.all()
    first_product_image = get_first_product_image()
    return products.annotate(image=Subquery(first_product_image.values('image')))

def get_cart_items(product_ids, cart_products):
    cart_items = []
    total_price = 0
    total_quantity = 0
    product_dict = {product.id: product for product in cart_products}

    for product_id, quantity in product_ids.items():
        product = product_dict.get(product_id)
        if product:
            cart_items.append({
                'product': product,
                'quantity': quantity,
            })
            total_price += product.price * quantity
            total_quantity += quantity

    return cart_items, total_price, total_quantity

def home(request):
    products_with_first_image = get_products_with_first_image()

    collections = Collection.objects.annotate(product_count=Count(
        'product')).filter(product_count__gt=0).order_by('id')

    for collection in collections:
        collection.products = collection.product_set.annotate(
            image=Subquery(get_first_product_image().values('image')))

    cart = get_user_cart(get_user_id())
    total_quantity = get_total_quantity(cart)

    return render(request, 'laptop_shop/home.html',
                  {'products': products_with_first_image, 'collections': collections, 'total_quantity': total_quantity})

class SignupPageView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def update_cart(request):
    cart = get_user_cart(get_user_id())
    product_ids = list(cart.keys())

    cart_products = Product.objects.filter(id__in=product_ids)

    cart_items, total_price, total_quantity = get_cart_items(cart, cart_products)

    cart_html = render_to_string('laptop_shop/partial_cart_list.html',
                                {'cart_items': cart_items, 'total_price': total_price, 'total_quantity': total_quantity})
    return JsonResponse({'cart_html': cart_html})

def index(request, collection_name):
    products = Product.objects.prefetch_related('images').filter(collection__name__iexact=collection_name)
    return render(request, 'laptop_shop/index.html', {'products': products})

def show(request, product_slug):
    product = get_object_or_404(Product, slug__iexact=product_slug)
    cart = get_user_cart(get_user_id())
    total_quantity = get_total_quantity(cart)
    return render(request, 'laptop_shop/show.html', {'product': product, 'total_quantity': total_quantity})

@ajax_login_required
def add_to_cart(request, user_id, product_id, increment=1):
    cart = cache.get(user_id, {'cart': {}})['cart']
    quantity = get_total_quantity(cart)

    if product_id not in cart:
        cart[product_id] = 0

    cart[product_id] += increment
    quantity += increment

    cache.set(user_id, {'cart': cart})

    return JsonResponse({'total_quantity': quantity})

def remove_from_cart(request, product_id):
    user_id = get_user_id()
    cart = get_user_cart(user_id)
    total_quantity = get_total_quantity(cart)
    quantity = 0

    if cart.get(product_id, 0):
        cart[product_id] -= 1
        quantity = max(0, cart[product_id])
        if quantity == 0:
            del cart[product_id]
        total_quantity -= 1

    cache.set(user_id, {'cart': cart})

    return JsonResponse({'total_quantity': total_quantity, 'quantity': quantity})
