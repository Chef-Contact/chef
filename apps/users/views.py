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
        user_role = request.POST.get('user_role')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        birthday = request.POST.get('birthday')
        month_of_birth = request.POST.get('month_of_birth')
        year_of_birth = request.POST.get('year_of_birth')

        # Basic input validation
        if not all([user_role, username, email, password, confirm_password]):
            return redirect('register')

        if password != confirm_password:
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
                return redirect('register')

        try:
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email уже зарегистрирован")

            verification_code = generate_verification_code()
            send_verification_email(email, verification_code)
            request.session['verification_code'] = verification_code
            request.session['registration_data'] = {
                'user_role': user_role,
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password,
                'birthday': birthday,
                'month_of_birth': month_of_birth,
                'year_of_birth': year_of_birth
            }
            return redirect('check_email')
        except ValidationError as e:
            print(f"Ошибка: {e}")
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
            registration_data = request.session.get('registration_data')
            if registration_data:
                user = User.objects.create(**registration_data)
                user.set_password(registration_data['password'])
                user.save()
                user = authenticate(username=registration_data['username'], password=registration_data['password'])
                if user:
                    login(request, user)
                    Shop.objects.create(user=user, design=4)
                    del request.session['verification_code']
                    del request.session['registration_data']
                    return redirect('becomeahost')
            return redirect('register')
        else:
            return redirect('check_email')
    return render(request, 'users/check-email.html', locals())

def send_verification_email(email, verification_code):
    send_mail(
        'Cheff Contact',
        f"""Здравствуйте.
        Ваш код для верификации: {verification_code}
        """,
        "noreply@somehost.local",
        [email]
    )

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
    if request.method == 'POST':
        if 'chat_chef' in request.POST:
            return create_chat(request, user)
    
    user_shop = user.shop_user
    
    if user_shop:
        design = user_shop.design
        if design:
            return render(request, f"shop/shop{design}.html", locals())
        else:
            return render(request, f"shop/shop4.html", locals())

    
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
            return redirect('edit', user.username)
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
        return redirect('profile_image', user.username)
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

def search_email(request):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    return render(request, 'users/reset_password.html', locals())


def write_code(request):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    return render(request, 'users/reset_password2.html', locals())


def new_password(request):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    return render(request, 'users/reset_password3.html', locals())


def security(request, username):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')

    if request.user.username != username:
        raise Http404("Нет доступа к данному профилю")
    
    user = get_object_or_404(User, username=username)

    if request.method == "POST":
        if 'update_password' in request.POST:
            password = request.POST.get('password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password == confirm_password:
                try:
                    user = User.objects.get(username = request.user)
                    if user.check_password(password):
                        user.set_password(new_password)
                        user.save()
                        return redirect('profile', user.username)
                    else:
                        return redirect('security', user.username)
                except:
                    return redirect('security', user.username)
            else:
                return redirect('security', user.username)

    return render(request, 'users/security.html', locals())


def invited(request):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    return render(request, 'host/invited.html', locals())



def booked_list(request):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    return render(request, 'users/booked_list.html', locals())


def transaction_out(request):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    return render(request, 'users/transaction_out.html', locals())
