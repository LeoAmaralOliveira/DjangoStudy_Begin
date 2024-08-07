from django import forms
from django.contrib.auth.models import User


class LoginForms(forms.Form):
    name_login = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: João Silva"}
        ),
    )
    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite sua senha"}
        ),
    )


class RegisterForms(forms.Form):
    register_name = forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: João Silva"}
        ),
    )
    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@xpto.com",
            }
        ),
    )
    password_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite sua senha"}
        ),
    )
    password_2 = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente",
            }
        ),
    )

    def clean_register_name(self):
        name = self.cleaned_data.get("register_name")
        if name:
            name = name.strip()
            if ' ' in name:
                raise forms.ValidationError(
                    "Espaços não são permitidos neste campo"
                )
            elif User.objects.filter(username=name).exists():
                raise forms.ValidationError("Usuário já existente")
            else:
                return name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("E-mail já existente")
            else:
                return email

    def clean_password_2(self):
        password_1 = self.cleaned_data.get("password_1")
        password_2 = self.cleaned_data.get("password_2")

        if password_1 and password_1:
            if password_1 != password_2:
                raise forms.ValidationError("As senhas não são iguais")
            else:
                return password_2
