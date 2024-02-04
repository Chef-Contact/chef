from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('reset/', reset, name="reset"),
]