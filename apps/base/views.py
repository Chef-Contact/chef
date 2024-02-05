from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base/index.html', context=None)

def about(request):
    return render(request, 'base/about.html', context=None)

def contact(request):
    return render(request, 'base/contact.html', context=None)

def test(request):
    return render(request, 'admin/index.html', context=None)

def host(request):
    return render(request, 'admin/index.html', context=None)

def public(request):
    return render(request, 'public/public.html', context=None)

def public_2(request):
    return render(request, 'public/public_2.html', context=None)

def chats(request):
    return render(request, 'chats/chats.html', context=None)

def chats_2(request):
    return render(request, 'chats/chats_2.html', context=None)

def becomeahost(request):
    return render(request, 'becomeahost.html', locals())

def search(request):
    return render(request, "search/index.html", locals())

def terms(request):
    return render(request, 'terms.html', locals())

def press(request):
    return render(request, 'press.html', locals())

def rules(request):
    return render(request, 'rules.html', locals())

def privacy(request):
    return render(request, 'privacy.html', locals())

def confiance(request):
    return render(request, 'confiance.html', locals())

def howitworks(request):
    return render(request, 'howitworks.html', locals())

def hospitality(request):
    return render(request, 'hospitality.html', locals())

def meal_restriction(request):
    return render(request, 'meal_restriction.html', locals())