from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.contrib import messages


class RegisterView(View):
    def get(self, request):
        return render(request, "register/index.html")

    def post(self, request):
        # messages.success(request, 'Email sent successfully.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
