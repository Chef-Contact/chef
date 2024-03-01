from django.urls import path
from apps.products.views import create_product,all_products

urlpatterns = [
    path('create_product/', create_product, name='create_product'),
    path('all_products/<str:username>/', all_products, name='all_products'),
]
