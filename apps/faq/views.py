from django.shortcuts import render

from apps.base.models import Settings
from .models import *


# Create your views here.
def faq(request):
    settings = Settings.objects.latest("id")
    faqs = FAQ.objects.all()
    return render(request, 'faq/faq.html', locals())

def faq_detail(request, id):
    settings = Settings.objects.latest("id")
    faqs = FAQ.objects.all()
    faq = FAQ.objects.get(id=id)
    return render(request, 'faq/faq_detail.html', locals())