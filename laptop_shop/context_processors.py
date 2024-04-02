from .models import Collection, Product
from django.core.cache import cache

def base_variables(request):
    if getattr(request, 'skip_base_variables', False):
        return {}
    
    try:
        collections = Collection.objects.values('name').all()
        products = Product.objects.values('name', 'slug').all()
        cart = get_user_cart(get_user_id(request))
        total_quantity = get_total_quantity(cart)
        return {
            'categories': collections,
            'search_products': products,
            'total_quantity': total_quantity
        }
    except Collection.DoesNotExist:
        return {}

def get_user_id(request):
    return request.session.get('user_id', None)

def get_user_cart(user_id):
    return cache.get(user_id, {'cart': {}})['cart']

def get_total_quantity(cart):
    return sum(cart.values()) | 0
