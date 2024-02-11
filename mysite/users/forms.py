from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={"class": "focus:outline-none", "placeholder": "mail@mail.com"}
    ))
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"class": "focus:outline-none", "placeholder": "Enter username"}
    ))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={"class": "focus:outline-none", "placeholder": "Enter Password"}
    ))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={"class": "focus:outline-none", "placeholder": "Confirm Password"}
    ))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class MyUserForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={"class": "focus:outline-none", "placeholder": "Enter username"}
    ))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={"class": "focus:outline-none", "placeholder": "Enter Password"}
    ))


