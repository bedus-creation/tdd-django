from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from front.forms.UserRegistrationForm import UserRegistrationForm


class RegisterView(View):
    def get(self, request):
        return render(request, "register/index.html")

    def post(self, request):
        forms = UserRegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(
                request, 'Registration has been completed. Please Login to continue.')
        return redirect('/register')
