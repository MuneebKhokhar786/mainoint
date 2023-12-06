
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:collection_name>/products', views.index, name='index'),
    path('products/<slug:product_slug>', views.show, name='show'),
    path('add-to-cart/<int:product_id>/<int:increment>', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart', views.update_cart, name='update_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('accounts/signup', views.SignupPageView.as_view(), name="signup"),
    path('accounts/', include("django.contrib.auth.urls")),
]
