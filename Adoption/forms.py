from .models import user, Animal
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class MyForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['img', 'species', 'breed', 'color', 'description',
                  'location', 'contact', 'availabilitystatus']
        widgets = {
            'uploadedby': forms.HiddenInput()
        }


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
