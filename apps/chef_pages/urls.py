from django.urls import path
from apps.chef_pages import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('shop_2/', views.shop_2, name='shop_2'),
    path('shop_3/', views.shop_3, name='shop_3'),
]