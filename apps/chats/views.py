from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import Message
from apps.users.models import User
from django.http import HttpResponseBadRequest

def chats_2(request):
    if request.method == 'POST':
        user = request.user
        content = request.POST.get('content', None)
        if content:
            message = Message.objects.create(sender=user, message=content)
            messages = Message.objects.all()
            user = User.objects.latest('id')
            context = {'messages': messages, 'user': user}
            return render(request, 'chats/chat.html', context)
        else:
            return HttpResponseBadRequest('Empty message')
    else:
        messages = Message.objects.all()
        user = User.objects.latest('id')
        context = {'messages': messages, 'user': user}
        return render(request, 'chats/chat.html', context)


