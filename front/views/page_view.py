from django.views import View
from django.shortcuts import render, redirect
from front.models.posts import Posts


class HomePageView(View):
    def get(self, request):
        posts = Posts.objects.all()
        return render(request, "home/index.html", {'posts': posts})
