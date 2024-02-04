from django.shortcuts import render
from .models import *

# Create your views here.
def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq/faq.html', locals())

def faq_detail(request, id):
    faqs = FAQ.objects.all()
    faq = FAQ.objects.get(id=id)
    return render(request, 'faq/faq_detail.html', locals())