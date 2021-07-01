'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    '''Register form class'''
    email = forms.EmailField()

    class Meta:
        '''Making line between the form and User model'''
        model = User
        fields = ["username", "email", "password1", "password2"]
