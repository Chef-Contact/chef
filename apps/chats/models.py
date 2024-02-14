from django.db import models
from apps.users.models import User
# Create your models here.
class Chat(models.Model):
    from_user = models.ForeignKey(
        User, 
        related_name = 'to_chats',
        on_delete = models.CASCADE
    )
    to_user = models.ForeignKey(
        User,
        related_name = 'from_chats',
        on_delete= models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name='Чат'
        verbose_name_plural='Чаты'

class Message(models.Model):
    user = models.ForeignKey(
        User,
        related_name ='messages',
        on_delete= models.CASCADE
    )
    text =models.CharField(
        max_length = 500
    )
    chat = models.ForeignKey(
        Chat,
        related_name = 'messages',
        on_delete = models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name='Сообщение'
        verbose_name_plural='Сообщения'