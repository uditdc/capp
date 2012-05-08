from django.db import models
from django import forms
# Create your models here.

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput())