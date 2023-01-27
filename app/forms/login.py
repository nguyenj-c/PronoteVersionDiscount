from django import forms
from django.forms import Form


class LoginForm(Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput)
    password = forms.CharField(label="Mot de Passe", max_length=50,
                               widget=forms.PasswordInput)

class RegisterForm(Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput())