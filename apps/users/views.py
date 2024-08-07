from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from apps.users.forms import LoginForms, RegisterForms


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form["name_login"].value()
            password = form["password"].value()

            user = auth.authenticate(
                request, username=username, password=password
            )

            if user:
                auth.login(request, user)
                messages.success(request, f"Seja bem vindo {username}!")
                return redirect('index')
            else:
                messages.error(request, "Erro ao efetuar login")
                return redirect('login')

    return render(request, 'users/login.html', {"form": form})


def register(request):
    form = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)
        if form.is_valid():
            register_name = form["register_name"].value()
            email = form["email"].value()
            password_1 = form["password_1"].value()

            user = User.objects.create_user(
                username=register_name, email=email, password=password_1
            )
            user.save()

            messages.success(request, "Cadastro efetuado com sucesso")
            return redirect('login')

    return render(request, 'users/register.html', {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Deslogado com sucesso")

    return redirect('login')
