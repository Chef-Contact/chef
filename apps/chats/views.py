from django.shortcuts import render, redirect
from .models import Chat, Message
# Create your views here.

def chat_detail(request, id):
    chat = Chat.objects.get(id=id)
    if request.method == 'POST':
        text = request.POST.get('text')
        Message.objects.create(text = text, user= request.user, chat = chat)
        return redirect('chat_detail', chat.id)
    return render(request, 'chats/chat.html', locals())

def create_chat(request, user):
    try:
        print('try1')
        try:
            print('try1-1')
            chat = Chat.objects.get(from_user = request.user, to_user = user)
            return redirect('chat_detail', chat.id)
        except:
            print('except1-1')
            chat = Chat.objects.get(to_user = request.user, from_user = user)
            return redirect('chat_detail', chat.id)
    except:
        print('except2')
        chat = Chat.objects.create(from_user = request.user, to_user = user)
        return redirect('chat_detail', chat.id)