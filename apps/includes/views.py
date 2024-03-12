from django.shortcuts import render, redirect
from apps.includes.models import HeaderTranslationModel
from apps.users.models import User
# Create your views here.
def header(request):
    header = HeaderTranslationModel.objects.latest("id")
    return render(request, 'include/header.html', locals())