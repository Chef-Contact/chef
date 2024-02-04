from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('test/', test, name="test"),
    path('host/', host, name="host"),
    path('public/', public, name="public"),
    path('public_2/', public_2, name="public_2"),
    path('chats/', chats, name="chats"),
    path('chats_2/', chats_2, name="chats_2"),
]