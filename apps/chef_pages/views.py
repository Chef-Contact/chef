from django.shortcuts import render

# Create your views here.

def shop(request):
    return render(request, "shop/shop.html", context=None)

def shop_2(request):
    return render(request, "shop/shop2.html", context=None)

def shop_3(request):
    return render(request, "shop/shop3.html", context=None)




