from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
# from django.contrib.auth.decorators import login_required


from .models import *
from apps.includes.models import HeaderTranslationModel, FooterTranslationModel
from apps.base.models import Settings
from apps.chats.views import create_chat
from apps.chef_pages.models import Shop,ShopDesign
import random

# Create your views here.
def generate_verification_code():
    return ''.join(random.choices('0123456789', k=4))

def register(request):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')

    if request.method == "POST":
        global user_role
        global username
        global email
        global password
        global confirm_password
        global birthday
        global month_of_birth
        global year_of_birth
        global verification_code
        user_role = request.POST.get('user_role')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        birthday = request.POST.get('birthday')
        month_of_birth = request.POST.get('month_of_birth')
        year_of_birth = request.POST.get('year_of_birth')
        verification_code = generate_verification_code()  # Генерация кода
        print(username, email, password, confirm_password)
        if password == confirm_password:
            if username and email and password and confirm_password:
                try:
                    if User.objects.filter(email=email).exists():
                        raise ValidationError("Email уже зарегистрирован")
                    
                    
                    send_mail(
                        'Cheff Contact',
                        f"""Здравствуйте.
                        Ваш код для верификации: {verification_code}

                        """,
                        "noreply@somehost.local",
                        [email]
                    )
                    # print(f"\n\n\n\n\n\\\n\n\n\n\n\n\n\n\n {email}\n\n\n\n\n\n\\nn\n\\n\n")
                    # Сохраняем код в сессию для последующей проверки
                    request.session['verification_code'] = verification_code
                    return redirect('check_email')
                except Exception as e:
                    print(f"Ошибка: {e}")
                    return redirect('register')
            else:
                print("Нет всех данных")
                return redirect('register')
        else:
            print("Пароли отличаются")
            return redirect('register')

    return render(request, 'users/register.html', locals())

def check_email(request):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    
    if request.method == "POST":
        entered_code = request.POST.get('verification_code')
        stored_code = request.session.get('verification_code')
        if entered_code == stored_code:
            user = User.objects.create(user_role=user_role, username=username, email=email, birthday=birthday, month_of_birth=month_of_birth, year_of_birth=year_of_birth)
                                                        
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            Shop.objects.create(user=request.user, design=4)
            # Код верный, продолжаем регистрацию
            del request.session['verification_code']  # Удаляем код из сессии
            # Здесь можете добавить дополнительные действия после успешной верификации
            return redirect('becomeahost')
        else:
            # Неправильный код, попробуйте снова
            return redirect('check_email')
    return render(request, 'users/check-email.html', locals())

def registration_success(request):
    return render(request, 'users/registration-success.html', locals())

def user_login(request):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:       
                return redirect('login')
        except User.DoesNotExist:
            return redirect('login')
    return render(request, 'users/login.html', locals())



def profile(request, username):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    user = User.objects.get(username = username)
    user_age = user.calculate_age()

    if request.method == 'POST':
        if 'send_message' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            question = request.POST.get('question')

            send_mail(
                'Cheff Contact',
                f"""Здравствуйте.
                Вам пришло новое сообщение от пользователя {name} .
                Его email: {email}
                Его номер телефона: {number}
                Сообщение: {question}

                """,
                "noreply@somehost.local",
                [user.email]
            )
            return redirect('profile', user.username)
    # if request.method == 'POST':
    #     return create_chat(request, user)
    
    user_shop = user.shop_user
    
    if user_shop:
        design = user_shop.design
        print('faesfsf /n/n/n/n/n/n/n'+design)
        return render(request, f"shop/shop{design}.html", locals())
    
    return render(request, 'users/index.html', locals())

def shop_edit(request, username):
    if request.user.username != username:
        raise Http404("Нет доступа к данному профилю")
    user = User.objects.get(username = username)
    shop = Shop.objects.get(user = user)
    shop_designs =  ShopDesign.objects.all()
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    if request.method == "POST":
        new_title = request.POST.get('title')
        new_tagline = request.POST.get('tagline')
        new_back_image = request.FILES.get('back_image')
        new_location = request.POST.get('location')
        new_description = request.POST.get('description')
        new_design = request.POST.get('design')
        
        try:
            shop.title = new_title
            shop.tagline = new_tagline
            shop.back_image = new_back_image
            shop.location = new_location
            shop.description = new_description
            shop.design = new_design
            
            shop.save()
            return redirect('index_step2')
        except Exception as e:
            print(f"Error saving user: {e}")
        return redirect('profile', user.username)
    

    
    return render(request, "shop/shop_edit.html", locals())

def edit_profile(request, username):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    user = get_object_or_404(User, username=username)
    if request.user.username != username:
        raise Http404("Нет доступа к данному профилю")
    
    if request.method == "POST":
        new_username = request.POST.get('username')
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_location = request.POST.get('location')
        new_job = request.POST.get('job')
        new_email = request.POST.get('email')
        new_biography = request.POST.get('biography')
        new_main_language = request.POST.get('main_language')
        new_year_of_birth = request.POST.get('year_of_birth')
        new_month_of_birth = request.POST.get('month_of_birth')
        new_birthday = request.POST.get('birthday')
        try:
            user.username = new_username
            user.first_name = new_first_name
            user.last_name = new_last_name
            user.job = new_job
            user.location = new_location
            user.email = new_email
            user.birthday = new_birthday
            user.month_of_birth = new_month_of_birth
            user.year_of_birth = new_year_of_birth
            user.main_language = new_main_language
            user.biography = new_biography
            user.save()
            return redirect('profile', user.username)
        except Exception as e:
            print(f"Error saving user: {e}")
        return redirect('profile', user.username)

    return render(request, 'users/edit.html', locals())

def edit_profile_image(request, username):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')

    if request.user.username != username:
        raise Http404("Нет доступа к данному профилю")
    
    user = get_object_or_404(User, username=username)

    if request.method == "POST":
        profile_image = request.FILES.get('profile_image')
        print(profile_image, "test profile_image")
        user.profile_image = profile_image
        user.save()
        return redirect('profile', user.username)
    return render(request, 'users/pic.html', locals())
    

def verification(request, username):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')

    if request.user.username != username:
        raise Http404("Нет доступа к данному профилю")
    
    user = get_object_or_404(User, username=username)
    return render(request, 'users/verification.html', locals())


def logout_view(request):
    logout(request)
    return redirect('index')


def reset(request):
    return render(request, 'users/reset.html', locals())


def dishes(request):
    return render(request, 'users/', locals())
