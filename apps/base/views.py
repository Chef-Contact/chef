from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from apps.includes.models import HeaderTranslationModel, FooterTranslationModel
from django.db.models import Q

from apps.base import models
from apps.base.task import send_contact_email

from apps.users.models import User
from apps.chats.models import Chat
from apps.products.models import Product, Kind, Category


# Create your views here.
def index(request):
    settings = models.Settings.objects.latest("id")
    become_all = models.Become.objects.all()
    become_active = models.BecomeActive.objects.all()
    perfect_all = models.Perfect.objects.all()
    perfect_active = models.Perfect.objects.all()[:3]
    work_all = models.Work.objects.all()
    cooking_active = models.CookingActive.objects.all()
    cooking_all = models.Cooking.objects.all()
    benefist_all = models.Benefist.objects.all()
    gellary_all = models.Gellary.objects.all()
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    first_categories = Category.objects.all()[:4]
    second_categories = Category.objects.all()[4:]
    if request.method == 'POST':
        print('test 1')
        if 'becomeahost2' in request.POST:
            user = User.objects.get(id = request.user.id)
            print('test')
            user.user_role = 'chef'
            user.save()
            return redirect('becomeahost')
    return render(request, 'base/index.html', locals())

def about(request):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    about = models.About.objects.latest("id")
    return render(request, 'base/about.html', locals())

def contact(request: HttpRequest):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    if request.method == "POST":
        last_name = request.POST.get('form[nom]')
        email = request.POST.get('form[email]')
        number = request.POST.get('form[tel]')
        message = request.POST.get('form[message]')

        send_mail(
            'Cheff Contact',
            f"""Здравствуйте.
            Спасибо за обратную связь, мы скоро свами свяжемся.
            Ваше ФИО: {last_name}
            Ваш email: {email}
            Ваш номер телефона: {number}
            Ваше сообщение: {message}...

            Если вы ошиблись при указании данных можете обратно зайти на сайт и оставить новый отзыв с исправленными 
            данными! """,
            "noreply@somehost.local",
            ["nurlanuuulubeksultan@gmail.com"]
        )
        # Вызов задачи Celery для обработки формы с данными
        send_contact_email.delay(last_name, email, number, message)

        return redirect('index')
    return render(request, 'base/contact.html', locals())

def meal_restriction(request):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    specefic = models.Specefic.objects.latest('id')
    return render(request, 'meal_restriction.html', locals())

def hospitality(request):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    hospitaly = models.Hospitaly.objects.latest('id')
    return render(request, 'hospitality.html', locals())

def terms(request):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    terms_id = models.Policies.objects.latest("id")
    return render(request, "terms.html", locals())


def privacy(request):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    privacy_id = models.Privacy.objects.latest("id")
    return render(request, 'privacy.html', locals())

def howitworks(request):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    howitworks = models.Howitworks.objects.latest('id')
    object_all = models.HowitworksObject.objects.all()
    quests_all = models.GuestsHosts.objects.all()
    return render(request, 'howitworks.html', locals())


def test(request):
    return render(request, 'admin/index.html', context=None)


def host(request):
    return render(request, 'admin/index.html', context=None)


def public(request):
    return render(request, 'public/public.html', context=None)


def public_2(request):
    return render(request, 'public/public_2.html', context=None)


def chats(request):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    if request.user.is_authenticated:
        chats = Chat.objects.all().filter(Q(from_user = request.user) | Q(to_user=request.user))
        return render(request, 'chats/index.html',  locals())
    else:
        return redirect('index')


def search(request):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    products = Product.objects.all()

    kinds = Kind.objects.all()
    categories = Category.objects.all()


    if request.method == 'POST':
        user_min_price =  request.POST.get('minprice')
        user_max_price =  request.POST.get('maxprice')
        title_filter = request.POST.get('title', '')
        category_filter = request.POST.get('category', None)
        kind_filter = request.POST.get('kind', None)

        filter_expr = Q()

        if title_filter:
            filter_expr |= Q(title__icontains=title_filter)

        if category_filter:
            filter_expr |= Q(category_id=category_filter)

        if kind_filter:
            filter_expr |= Q(kind_id=kind_filter)

        if user_min_price and user_max_price:
            filter_expr &= Q(price__range=(user_min_price, user_max_price))

        products = products.filter(filter_expr)
        
    return render(request, "search/index.html", locals())

def press(request):
    return render(request, 'press.html', locals())


def rules(request):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    
    rule = models.Rules.objects.latest('id')
    return render(request, 'rules.html', locals())

def hospitality(request):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')

    hospitaly = models.Hospitaly.objects.latest('id')
    return render(request, 'hospitality.html', locals())


def meal_restriction(request):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')

    specefic = models.Specefic.objects.latest('id')
    return render(request, 'meal_restriction.html', locals())

def trustsafety(request):
    settings = models.Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')

    trust = models.TrustSafety.objects.latest('id')
    insurance_object = models.InsuranceObjects.objects.all()
    trust_object = models.TrustSafetyObjects.objects.all()
    return render(request, 'confiance.html', locals())


