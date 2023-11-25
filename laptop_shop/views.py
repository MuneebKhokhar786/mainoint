from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from django.db.models import Count, OuterRef, Subquery
from .models import Product, Collection, ProductImage


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

    product_ids = list(cart.keys())
    cart_items = []
    total_price = 0

    cart_products = Product.objects.prefetch_related('images').filter(id__in=product_ids)

    for product in cart_products:
        quantity = cart[str(product.id)]
        cart_items.append({
            'product': product,
            'quantity': quantity,
        })
        total_price +=  product.price * quantity
    return render(request, 'laptop_shop/home.html',
                {'products': products_with_first_image, 'collections': collections,
                    'cart_items': cart_items, 'total_price': total_price})


def index(request, collection_name):
    products = Product.objects.prefetch_related('images').filter(collection__name__iexact=collection_name)
    return render(request, 'laptop_shop/index.html', {'products': products})


def show(request, product_slug):
    product = Product.objects.prefetch_related().get(slug__iexact=product_slug)
    return render(request, 'laptop_shop/show.html', {'product': product})


def add_to_cart(request):
    product_id = request.POST.get('product_id')
    cart = cache.get('cart', {})

    if not cart.get(product_id, {}):
        cart[product_id] = 1
    else:
        cart[product_id] += 1

    cache.set('cart', cart)

    return JsonResponse({'message': 'Product added to cart successfully'})

