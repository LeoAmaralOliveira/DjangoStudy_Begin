from django.shortcuts import render
from users.forms import LoginForms, RegisterForms


def login(request):
    form = LoginForms()
    return render(
        request,
        'users/form.html',
        {"form": form, "button_text": "Login"}
    )


def register(request):
    form = RegisterForms()
    return render(
        request,
        'users/form.html',
        {"form": form, "button_text": "Criar sua conta"}
    )
