from django.shortcuts import render, get_object_or_404
from .decorators import ajax_login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
import json
from django.db.models import Count, OuterRef, Subquery
from accounts.models import CustomUser as User
from .models import Product, Collection, ProductImage, Order, OrderItem
from django.core.mail import send_mail
from django.core.cache import cache

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


def update_cart(request):
    cart = get_user_cart(get_user_id())
    product_ids = list(cart.keys())

    cart_products = Product.objects.filter(id__in=product_ids)

    cart_items, total_price, total_quantity = get_cart_items(cart, cart_products)

    cart_html = render_to_string('laptop_shop/partial_cart_list.html',
                                {'cart_items': cart_items, 'total_price': total_price, 'total_quantity': total_quantity})
    return JsonResponse({'cart_html': cart_html})

def checkout(request):
    cart_items = json.loads(request.POST.get('items'))
    total_price = request.POST.get('total')
    checkout_html = render_to_string('laptop_shop/checkout.html', {'cart_items': cart_items, 'total_price': total_price})
    return JsonResponse({'checkout_html': checkout_html})

def index(request, collection_name):
    products = Product.objects.prefetch_related('images').filter(collection__name__iexact=collection_name)
    return render(request, 'laptop_shop/index.html', {'products': products})

def contact(request):
    return render(request, 'laptop_shop/contact.html')

def send_email(request):
    data = json.loads(request.body)
    subject = data.get('name') + ' - ' + data.get('email')
    message = data.get('message')
    recipient_list = ['dev.muneeb.khokhar@gmail.com']

    send_mail(subject, message, 'dev.muneeb.khokhar@gmail.com', recipient_list)
    return JsonResponse({'message': 'Email sent successfully!'})

def show(request, product_slug):
    product = get_object_or_404(Product, slug__iexact=product_slug)
    cart = get_user_cart(get_user_id())
    total_quantity = get_total_quantity(cart)
    return render(request, 'laptop_shop/show.html', {'product': product, 'total_quantity': total_quantity})

@ajax_login_required
def add_to_cart(request, user_id, product_id, increment=1):
    cart = get_user_cart(user_id)
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

@ajax_login_required
def create_order(request, user_id, payment_method, total_price):
    cart = get_user_cart(user_id)

    product_ids = list(cart.keys())
    products = Product.objects.filter(id__in=product_ids)

    user = User.objects.get(id=user_id)

    order = Order.objects.create(user=user, total_price=float(total_price), payment_method=payment_method)
    order_items = []
    for product in products:
        quantity = cart[product.id]
        order_item = OrderItem(order=order, product=product, quantity=quantity)
        order_items.append(order_item)
    OrderItem.objects.bulk_create(order_items)

    cache.delete(user_id)

    return JsonResponse({'message': 'Order created successfully!'})
