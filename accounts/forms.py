from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # labels = {
        #     'username': 'Username',
        #     'email': '',
        #     'password1': '',
        #     'password2': '',
        # }
        # widgets = {
        #     'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
        #     'email': forms.TextInput(attrs={'placeholder': 'Enter your email'}),
        #     'password1': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        #     'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        # }
        # help_texts = {
        #     'username': '',
        #     'email': '',
        #     'password1': '',
        #     'password2': '',
        # }

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("image",'bio')