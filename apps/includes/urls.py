from django.urls import path

from apps.includes.views import header

urlpatterns = [
    path('header/', header, name='header'),
]
