from django.shortcuts import render
from django.db.models import Count, OuterRef, Subquery
from .models import Product, Collection, ProductImage, ProductVideo


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
    return render(request, 'laptop_shop/home.html', {'products': products_with_first_image, 'collections': collections})


def index(request, collection_name):
    products = Product.objects.filter(collection__name__iexact=collection_name)
    first_product_image = ProductImage.objects.filter(
        product=OuterRef('pk')).order_by('id')[:1]
    products_with_first_image = products.annotate(
        image=Subquery(first_product_image.values('image')))

    return render(request, 'laptop_shop/index.html', {'products': products_with_first_image})


def show(request, product_slug):
    product = Product.objects.get(slug__iexact=product_slug)
    product_images = ProductImage.objects.filter(
        product=product).values('image')
    product_videos = ProductVideo.objects.filter(
        product=product).values('video')
    return render(request, 'laptop_shop/show.html',
                    {'product': product, 'product_images': product_images, 'product_videos': product_videos})
