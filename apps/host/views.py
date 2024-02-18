from django.shortcuts import render, redirect
from apps.chats.views import create_chat
from apps.host import models
from apps.base import models as models_base

# Create your views here.
def becomeahost(request):
    become = models.BecomeaHost.objects.latest("id")
    free_all = models.Free.objects.all()
    guests_all = models.Guests.objects.all()
    receive_all = models.Receive.objects.all()
    end_all = models.BecomeEnd.objects.all()
    blog_active = models.BlogActive.objects.all()
    blog_all= models.Blog.objects.all()
    # price_all = models.PriceFood.objects.all()

    perfect_all = models_base.PerfectActive.objects.all()
    perfect_latest = models_base.Perfect.objects.latest("id")
    return render(request, 'becomeahost.html', locals())

def index_event(request):
    index_host = models.Host.objects.latest('id')
    return render(request, 'host/index.html', locals())

def make_event(request):
    index_host = models.Host.objects.latest('id')
    print('feasfesa')
    if request.method =="POST":
        print('feasfesa2112')
        question_1 = request.POST.get('question_1')
        question_2 = request.POST.get('question_2')
        question_3 = request.POST.get('question_3')
        question_4 = request.POST.get('question_4')
        question_5 = request.POST.get('question_5')
        question_6 = request.POST.get('question_6')
        question_7 = request.POST.get('question_7')
        question_8 = request.POST.get('question_8')
        question_9 = request.POST.get('question_9')
        question_10 = request.POST.get('question_10')
        question_11 = request.POST.get('question_11')
        question_12 = request.POST.get('question_12')
        models.ChefRegister.objects.create(user=request.user, question_1=question_1, question_2=question_2, question_3=question_3, question_4=question_4, question_5=question_5, question_6=question_6, question_7=question_7, question_8=question_8, question_9=question_9, question_10=question_10, question_11=question_11, question_12=question_12)
        return redirect('index')

    return render(request, 'host/shef_register.html', locals())

def event_detail(request, id):
    event = models.ChefRegister.objects.get(id=id)
    if request.method == 'POST':
        return create_chat(request, event.user)
    return render(request, 'host/event_detail.html', locals())