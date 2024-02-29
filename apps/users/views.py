from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import Http404
from django.shortcuts import get_object_or_404
# from django.contrib.auth.decorators import login_required


from .models import *
from apps.includes.models import HeaderTranslationModel, FooterTranslationModel
from apps.base.models import Settings
from apps.chats.views import create_chat
from apps.chef_pages.models import Shop,ShopDesign

# Create your views here.
def register(request):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')

    if request.method == "POST":
        user_role = request.POST.get('user_role')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        birthday = request.POST.get('birthday')
        month_of_birth = request.POST.get('month_of_birth')
        year_of_birth = request.POST.get('year_of_birth')
        print(username, email, password, confirm_password)
        if password == confirm_password:
            if username and email and password and confirm_password:
                try:
                    user = User.objects.create(user_role = user_role, username = username, email = email, birthday = birthday, month_of_birth = month_of_birth, year_of_birth = year_of_birth)
                    user.set_password(password)
                    user.save()
                    user = User.objects.get(username = username)
                    user = authenticate(username = username, password = password)
                    login(request, user)
                    Shop.objects.create(user=request.user)
                    return redirect('index')
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

def user_login(request):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        except:
            return redirect('login')
    return render(request, 'users/login.html', locals())



def profile(request, username):
    settings = Settings.objects.latest("id")
    header = HeaderTranslationModel.objects.latest("id")
    footer = FooterTranslationModel.objects.latest('id')
    user = User.objects.get(username = username)
    user_age = user.calculate_age()
    if request.method == 'POST':
        return create_chat(request, user)
    
    user_shop = user.shop_user
    
    if user_shop:
        design = user_shop.design
        return render(request, f"shop/shop{design if design != None else 1}.html", locals())
    
    return render(request, 'users/index.html', locals())

def shop_edit(request, username):
    if request.user.username != username:
        raise Http404("Нет доступа к данному профилю")
    user = User.objects.get(username = username)
    shop = Shop.objects.get(user = user)
    shop_designs =  ShopDesign.objects.all()
    if request.method == "POST":
        new_title = request.POST.get('title')
        new_back_image = request.FILES.get('back_image')
        new_location = request.POST.get('location')
        new_description = request.POST.get('description')
        new_design = request.POST.get('design')
        
        try:
            shop.title = new_title
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
