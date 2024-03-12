from django.urls import path
from .views import chat_detail,send_message,get_chat_messages

urlpatterns = [
    path('chat_detail/<int:id>/', chat_detail, name='chat_detail'),
    path('send_message/', send_message, name='send_message'),
    path('get_chat_messages/<int:chat_id>/', get_chat_messages, name='get_chat_messages'),
]
