from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Password', max_length=32)
