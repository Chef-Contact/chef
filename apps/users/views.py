from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


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


def logout_view(request):
    logout(request)
    return redirect('index')


def reset(request):
    return render(request, 'users/reset.html', context=None)

print("TEST")