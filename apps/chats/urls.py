from django.urls import path
from .views import chat_detail

urlpatterns = [
    path('chat_detail/<int:id>/', chat_detail, name='chat_detail')
]
