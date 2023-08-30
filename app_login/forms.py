from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import Account, AccountType


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name",
                  "last_name", "password1", "password2")


class AccountForm(forms.ModelForm):
    account_type = forms.ModelChoiceField(queryset=AccountType.objects.all(),
                                          empty_label="Select Type")

    class Meta:
        model = Account
        fields = ("account_type",)
