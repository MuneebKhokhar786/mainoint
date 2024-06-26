
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:collection_name>/products', views.index, name='index'),
    path('contact-us', views.contact, name='contact'),
    path('send-email', views.send_email, name='send_email'),
    path('products/<slug:product_slug>', views.show, name='show'),
    path('add-to-cart/<int:product_id>/<int:increment>', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart', views.update_cart, name='update_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('<str:collection_name>/filtered_products', views.filter_products, name='filter_products'),
    path('create-order/<str:payment_method>/<str:total_price>', views.create_order, name='create_order'),
]
