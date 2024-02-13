from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'message', 'timestamp')
    list_filter = ('sender', 'recipient', 'timestamp')