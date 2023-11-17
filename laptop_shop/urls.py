
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'collections', views.CollectionViewSet, basename='collection')

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:collection_name>/products/', views.index, name='index'),
    path('products/<slug:product_slug>/', views.show, name='show'),
    path('v1/api/', include(router.urls)),
]
