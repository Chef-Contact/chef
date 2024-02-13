from django.urls import path
from apps.chats.views import chats_2
urlpatterns = [
path('chat_index/', chats_2, name="chats_2"),

]


