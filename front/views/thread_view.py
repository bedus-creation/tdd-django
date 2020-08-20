from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib import messages
from django.shortcuts import render, redirect
from front.forms.ThreadCreateForm import ThreadCreateForm


class ThreadView(FormView):
    template_name = 'thread/create.html'
    form_class = ThreadCreateForm
    success_url = '/thread/create'

    def form_valid(self, form):
        messages.success(self.request, 'Congratulations ! Thread has been created.')
        return super().form_valid(form)

    # def get(self, request):
    #     form = ThreadCreateForm()
    #     return render(request, "thread/create.html", {'form': form})

    # def post(self, request):
    #     form = ThreadCreateForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(
    #             request, 'Congratulations ! Thread has been created.')
    #         return HttpResponseRedirect('/thread/create')
