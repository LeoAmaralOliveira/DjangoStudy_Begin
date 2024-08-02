from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from users.forms import LoginForms, RegisterForms


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form["name_login"].value()
            password = form["password"].value()

            user = auth.authenticate(
                request,
                username=username,
                password=password
            )

            if user:
                auth.login(request, user)
                messages.success(request, f"{username} logado com sucesso!")
                return redirect('index')
            else:
                messages.error(request, "Erro ao efetuar login")
                return redirect('login')

    return render(
        request,
        'users/form.html',
        {
            "form": form,
            "button_text": "Login",
            "dest_url": "login",
            "http_method": "POST"
        }
    )


def register(request):
    form = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)
        if form.is_valid():
            if form["password_1"].value() != form["password_2"].value():
                messages.error(request, "Senhas não são iguais")
                return redirect('register')

            register_name = form["register_name"].value()
            email = form["email"].value()
            password_1 = form["password_1"].value()

            if User.objects.filter(username=register_name).exists():
                messages.error(request, "Usuário já existente")
                return redirect('register')

            user = User.objects.create_user(
                username=register_name,
                email=email,
                password=password_1
            )
            user.save()

            messages.success(request, "Cadastro efetuado com sucesso")
            return redirect('login')

    return render(
        request,
        'users/form.html',
        {
            "form": form,
            "button_text": "Criar sua conta",
            "dest_url": "register",
            "http_method": "POST"
        }
    )


def logout(request):
    auth.logout(request)
    messages.success(request, "Deslogado com sucesso")

    return redirect('login')
