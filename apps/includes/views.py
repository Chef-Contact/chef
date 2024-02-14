from django.shortcuts import render

from apps.includes.models import HeaderTranslationModel

# Create your views here.
def header(request):
    header = HeaderTranslationModel.objects.latest("id")
    return render(request, 'include/header.html', locals())