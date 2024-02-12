from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
from apps.users.models import User

def chat_view(request):
    messages = Message.objects.all()
    user = User.objects.latest('id')
    context = {'messages': messages, 'user': user}
    return render(request, 'chats/chat.html', context)

def send_message(request):
    if request.method == 'POST':
        user = request.user
        content = request.POST.get('content', None)
        if content:
            message = Message.objects.create(sender=user, message=content)
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})

