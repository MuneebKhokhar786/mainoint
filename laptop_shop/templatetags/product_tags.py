from django import template

register = template.Library()

@register.filter
def get_product_image(product):
    if hasattr(product, 'image') and product.image:
        return product.image.url
    elif hasattr(product, 'images') and product.images.exists():
        return product.images.first().image.url
    return ''