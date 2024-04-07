from django.urls import path
from apps.products.views import create_product, all_products, product_detail, edit_product, all_products_edit

urlpatterns = [
    path('create_product/', create_product, name='create_product'),
    path('all_products/<str:username>/', all_products, name='all_products'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('all_products_edit/<str:username>/', all_products_edit, name='all_products_edit'),
    path('edit_product/<int:id>/', edit_product, name='edit_product'),
]
