from django.shortcuts import render

from apps.base.models import Settings
from apps.includes.models import HeaderTranslationModel, FooterTranslationModel

# Create your views here.
def cart(request):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    cart = True
    return render(request, 'cart/cart.html', locals())