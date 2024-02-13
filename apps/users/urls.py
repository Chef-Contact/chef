from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('reset/', reset, name="reset"),
    path('logout/', logout_view, name='logout'),
    path('profile/<str:username>/', profile, name='profile'),
    path('edit/<str:username>/', edit_profile, name='edit'),
    path('flat_book/', flat_book, name='flat_book'),

]