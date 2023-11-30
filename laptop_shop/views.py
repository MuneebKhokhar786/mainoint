from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.db.models import Count, OuterRef, Subquery
from .models import Product, Collection, ProductImage
from django.contrib.auth.forms import UserCreationForm


def home(request):
    products = Product.objects.all()
    first_product_image = ProductImage.objects.filter(
        product=OuterRef('pk')).order_by('id')[:1]
    products_with_first_image = products.annotate(
        image=Subquery(first_product_image.values('image')))

    collections = Collection.objects.annotate(product_count=Count(
        'product')).filter(product_count__gt=0).order_by('id')
    for collection in collections:
        collection_with_first_image = collection.product_set.annotate(
            image=Subquery(first_product_image.values('image')))
        collection.products = collection_with_first_image

    cart = cache.get('cart', {})
    total_quantity = sum(cart.values())

    return render(request, 'laptop_shop/home.html',
                {'products': products_with_first_image, 'collections': collections, 'total_quantity': total_quantity})


class SignupPageView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def update_cart(request):
    cart = cache.get('cart', {})

    product_ids = list(cart.keys())
    total_price = 0
    total_quantity = 0
    cart_items = []

    if product_ids:
        cart_products = Product.objects.filter(id__in=product_ids).prefetch_related('images')
        product_dict = {product.id: product for product in cart_products}

        for product_id, quantity in cart.items():
            product = product_dict.get(product_id)
            if product:
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                })
                total_price += product.price * quantity
                total_quantity += quantity

    cart_html = render_to_string('laptop_shop/partial_cart_list.html',
                                {'cart_items': cart_items, 'total_price': total_price, 'total_quantity': total_quantity})
    return JsonResponse({'cart_html': cart_html})

def index(request, collection_name):
    products = Product.objects.prefetch_related('images').filter(collection__name__iexact=collection_name)
    return render(request, 'laptop_shop/index.html', {'products': products})

@login_required
def show(request, product_slug):
    product = Product.objects.prefetch_related().get(slug__iexact=product_slug)
    cart = cache.get('cart', {})
    total_quantity = sum(cart.values())
    return render(request, 'laptop_shop/show.html', {'product': product, 'total_quantity': total_quantity})


def add_to_cart(request, product_id, increment=1):
    cart = cache.get('cart', {})
    quantity = sum(cart.values())

    if not cart.get(product_id, 0):
        cart[product_id] = increment
    else:
        cart[product_id] += increment

    quantity += increment

    cache.set('cart', cart)

    return JsonResponse({'total_quantity': quantity})

def remove_from_cart(request, product_id):
    cart = cache.get('cart', {})
    total_quantity = sum(cart.values())
    quantity = 0

    if cart.get(product_id, 0):
        cart[product_id] -= 1
        quantity = cart[product_id]
        if quantity == 0:
            del cart[product_id]
        total_quantity -= 1

    cache.set('cart', cart)

    return JsonResponse({'total_quantity': total_quantity, 'quantity': quantity})



