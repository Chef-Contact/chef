from django.db import models
from apps.users.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.CharField(
        max_length=255,   
        verbose_name='Администрация',
        default='админ'
    )
    message = models.TextField(verbose_name='Сообщение')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время отправки')
        
    def __str__(self):
        return f'{self.sender.username} -> {self.recipient}: {self.message}'
    
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
