from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('reset/', reset, name="reset"),
    path('dishes/', dishes, name="dishes"),
    path('logout/', logout_view, name='logout'),
    path('profile/<str:username>/', profile, name='profile'),
    path('shop_edit/<str:username>/', shop_edit, name='shop_edit'),
    path('edit/<str:username>/', edit_profile, name='edit'),
    path('profile_image/<str:username>/', edit_profile_image, name='profile_image'),
    path('verification/<str:username>/', verification, name='verification'),
]