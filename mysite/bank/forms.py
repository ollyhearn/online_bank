from django import forms
from .models import *


class AddUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['FIO', 'phone_number', 'card_number', 'mail', 'password']

