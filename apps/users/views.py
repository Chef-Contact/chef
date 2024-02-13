from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import Http404
from django.shortcuts import get_object_or_404
# from django.contrib.auth.decorators import login_required


from .models import *

# Create your views here.
def register(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(username, email, password, confirm_password)
        if password == confirm_password:
            if username and email and password and confirm_password:
                try:
                    user = User.objects.create(username = username, email = email)
                    user.set_password(password)
                    user.save()
                    user = User.objects.get(username = username)
                    user = authenticate(username = username, password = password)
                    login(request, user)
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

    return render(request, 'users/register.html', context=None)

def user_login(request):
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
    return render(request, 'users/login.html', context=None)



def profile(request, username):
    user = User.objects.get(username = username)
    return render(request, 'users/index.html', locals())


def edit_profile(request, username):
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
        try:
            user.username = new_username
            user.first_name = new_first_name
            user.last_name = new_last_name
            user.job = new_job
            user.location = new_location
            user.email = new_email
            user.biography = new_biography
            user.save()
            return redirect('profile', user.username)
        except Exception as e:
            print(f"Error saving user: {e}")
        return redirect('profile', user.username)

    return render(request, 'users/edit.html', locals())


def logout_view(request):
    logout(request)
    return redirect('index')


def reset(request):
    return render(request, 'users/reset.html', context=None)

def flat_book(request):
    return render(request, 'users/flat_booked.html', locals())