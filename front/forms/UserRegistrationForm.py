from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': '-mx-6 px-8  w-full border rounded px-3 py-2 text-gray-700 focus:outline-none',
            'placeholder': "Email"
        }))
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
