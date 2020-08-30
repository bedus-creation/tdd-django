from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib import messages
from django.shortcuts import render, redirect
from front.forms.ThreadCreateForm import ThreadCreateForm


class ThreadView(FormView):
    template_name = 'thread/create.html'
    form_class = ThreadCreateForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'Congratulations ! Thread has been created.')
        return super().form_valid(form)
