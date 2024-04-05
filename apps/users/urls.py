from django.urls import path
from django.contrib.auth import views as auth_views

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
    path('check_email/', check_email, name='check_email'),
    path('search_email/', search_email, name='search_email'),
    path('write_code/', write_code, name='write_code'),
    path('new_password/', new_password, name='new_password'),
    path('security/<str:username>/', security, name='security'),
    path('user_foods/', user_foods, name='user_foods'),
    path('invited/', invited, name='invited'),
    path('booked_list/', booked_list, name='booked_list'),
    path('invitedDetail/', invitedDetail, name='invitedDetail'),

    path('transaction_out/', transaction_out, name='transaction_out'),



    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]