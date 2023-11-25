
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:collection_name>/products/', views.index, name='index'),
    path('products/<slug:product_slug>/', views.show, name='show'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]
