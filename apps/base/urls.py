from django.urls import path

from .views import *
# from apps.chats.views import chat_view

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('terms/', terms, name='terms'),
    path('privacy/', privacy, name='privacy'),
    path('contact/', contact, name="contact"),
    path('test/', test, name="test"),
    path('host/', host, name="host"),
    path('public/', public, name="public"),
    path('public_2/', public_2, name="public_2"),
    path('chats/', chats, name="chats"),
    path('search/', search, name='search'),
    path('press/', press, name='press'),
    path('rules/', rules, name='rules'),
    path('confiance/', trustsafety, name='confiance'),
    path('howitworks/', howitworks, name='howitworks'),
    path('hospitality/', hospitality, name='hospitality'),
    path('meal_restriction/', meal_restriction, name='meal_restriction'),
    path('video/', video, name='video'),

]