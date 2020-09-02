from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = (
            'username',
            'email',
            'password'
        )
    # username = forms.CharField(max_length=50, label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    # email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={"class": "form-control"}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))




