from django.shortcuts import render, redirect
from  apps.base.models import Contact
from django.core.mail import send_mail
from apps.base import models 


# Create your views here.
def index(request):
    settings = models.Settings.objects.latest("id")
    become = models.Become.objects.all()
    perfect_all = models.Perfect.objects.all()
    return render(request, 'base/index.html', locals())


def video(request):
    return render(request, 'home_video.html', locals())


def about(request):
    return render(request, 'base/about.html', context=None)


def contact(request):
    # if request.method == "POST":
    #     last_name = request.POST.get('form[nom]')
    #     email = request.POST.get('form[email]')
    #     number = request.POST.get('form[tel]')
    #     message = request.POST.get('form[message]')
    #     Contact.objects.create(last_name=last_name, email=email, number=number, message=message)
    #     send_mail(
    #         f'{message}',
    #         f"""Здравствуйте.
    #         Спасибо за обратную связь, мы скоро свами свяжемся.
    #         Ваще ФИО: {last_name}
    #         Ваще email: {email}
    #         Ваш номер телефона: {number}
    #         Ваще сообщение: {message}...

    #         Если вы ошиблись при указании данных можете обратно зайти на сайт и оставить новый отзыв с исправленными данными!
    #         """,
    #         "noreply@somehost.local",
    #         [email]
    #     )
    #     return redirect('contact')
    return render(request, 'base/contact.html', context=None)


def terms(request):
    terms_id = models.Policies.objects.latest("id")
    return render(request, "terms.html", locals())

def privacy(request):
    privacy_id = models.Privacy.objects.latest("id")
    return render(request, 'privacy.html', locals())

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


def press(request):
    return render(request, 'press.html', locals())

def rules(request):
    return render(request, 'rules.html', locals())


def confiance(request):
    return render(request, 'confiance.html', locals())

def howitworks(request):
    return render(request, 'howitworks.html', locals())

def hospitality(request):
    return render(request, 'hospitality.html', locals())

def meal_restriction(request):
    return render(request, 'meal_restriction.html', locals())