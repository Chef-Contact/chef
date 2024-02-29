from django.shortcuts import render

# Create your views here.
def cart(request):
    cart = True
    return render(request, 'cart/cart.html', locals())