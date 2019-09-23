from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from . models import Blog


def Index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "hello.html", {})


class BloglDetailView(View):
    template_name = "show.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_articles'] =
    #     return context
    def get(self, request, pk, slug):
        data = Blog.objects.filter(id=pk)
        return render(request, "show.html", {'data': data})

    # def show(self, request):
    #     return render(request, "show.html", {})
