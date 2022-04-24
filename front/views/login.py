from front.forms.LoginForm import LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Login(FormView):
    template_name = "login/index.html"
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = form.cleaned_data.get('user')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError('This email address doesn\'t exists.')

        if user.check_password(password):
            raise ValidationError('This password doesn\'t match')

        login(self.request, user)

        return redirect('/')
