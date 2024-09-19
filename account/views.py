from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterUSForm, LoginUSForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def account_register(request):
    if request.method == 'POST':
        form = RegisterUSForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Регистрация прошла успешно.')
            login(request, user)  # Foydalanuvchini tizimga kiritish
            return redirect('home')
        else:
            messages.error(request, 'Регистрация не удалась. Пожалуйста, исправьте ошибки ниже.')
    else:
        form = RegisterUSForm()

    return render(request, 'account/register.html', {'form': form})
def account_login(request):
    if request.method == 'POST':
        form = LoginUSForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Теперь вы вошли в систему как {username}.')
                return redirect('home')
            else:
                messages.error(request, 'неправильное имя пользователя или пароль.')
        else:
            messages.error(request, 'неправильное имя пользователя или пароль.')
    else:
        form = LoginUSForm()

    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Вы успешно вышли из системы.')
    return redirect('home')


