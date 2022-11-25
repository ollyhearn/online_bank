from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['FIO', 'phone_number', 'card_number', 'mail', 'password']


class RegistrationUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
