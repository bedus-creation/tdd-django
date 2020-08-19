from django.views import View
from django.shortcuts import render, redirect


class HomePageView(View):
    def get(self, request):
        return render(request, "home/index.html")
