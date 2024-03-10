from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from apps.includes.models import HeaderTranslationModel, FooterTranslationModel

from .models import Chat, Message
import json
# Create your views here.

def chat_detail(request, id):
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    chat = Chat.objects.get(id=id)
    return render(request, 'chats/chat.html', locals())

def get_chat_messages(request, chat_id):
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    chat = Chat.objects.get(id=chat_id)
    user_id = request.user.id
    messages = list(chat.messages.all().order_by('created').values('text', 'created', 'user_id'))
    for message in messages:
        message['created'] = message['created'].strftime('%b %d %H:%M')
    return JsonResponse({'messages': messages, 'user_id': user_id})

def create_chat(request, user):
    try:
        try:
            chat = Chat.objects.get(from_user = request.user, to_user = user)
            return redirect('chat_detail', chat.id)
        except:
            chat = Chat.objects.get(to_user = request.user, from_user = user)
            return redirect('chat_detail', chat.id)
    except:
        chat = Chat.objects.create(from_user = request.user, to_user = user)
        return redirect('chat_detail', chat.id)
    
@require_http_methods(["POST"])
def send_message(request):
    try:
        data = json.loads(request.body)
        user_id = data.get('user_id')
        chat_id = data.get('chat_id')
        message = data.get('message')

        if not user_id or not message:
            return JsonResponse({'status': 'error', 'message': 'Отсутствуют обязательные параметры'}, status=400)
        else:
            Message.objects.create(text=message, user_id = int(user_id), chat_id =chat_id )
        return JsonResponse({'status': 'success', 'message': message})

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Неверный формат данных'}, status=400)