import re
from django import forms
from registration.forms import RegistrationForm
from django.contrib.auth.models import User
from quizapp.models import avatar


class MyRegistrationForm(RegistrationForm):
    required_css_class = 'required'
    email = forms.EmailField(label="E-mail")
    first_name = forms.CharField(label='first name')
    last_name = forms.CharField(label='first name')
    username = forms.CharField(label='username')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', "email")


class ProfileForm(forms.Form):
    firstName = forms.CharField(label='first name')
    lastName = forms.CharField(label="last name")
    avatar = forms.CharField(label='avatar')


class ScoreUpdate(forms.Form):
    score = forms.IntegerField(label='score')
