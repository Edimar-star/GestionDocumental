from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={
        'name': 'username',
        'class': 'input'
        }))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'name': 'password',
        'class': 'input'
        }))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'name': 'password',
        'class': 'input'
        }))

    class Meta:
        model= User
        fields=['username','password1', 'password2']
        help_texts={k:"" for k in fields}