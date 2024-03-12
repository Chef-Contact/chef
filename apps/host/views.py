from django.shortcuts import render, redirect
from apps.chats.views import create_chat
from apps.host import models
from apps.base import models as models_base
from apps.includes.models import HeaderTranslationModel, FooterTranslationModel


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
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    return render(request, 'becomeahost.html', locals())

def index_step1(request):
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    index_host = models.Host.objects.latest('id')
    return render(request, 'host/index_step1.html', locals())

def index_step2(request):
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    index_host = models.Host.objects.latest('id')
    return render(request, 'host/index_step2.html', locals())