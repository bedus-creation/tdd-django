from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.contrib import messages
from front.forms.UserRegistrationForm import UserRegistrationForm


def get(request):
    return render(request, "register/index.html")


class Register(FormView):
    template_name = "register/index.html"
    form_class = UserRegistrationForm

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'Registration has been completed. Please Login to continue.')

        return redirect('/register')
