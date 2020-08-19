from django.urls import path
from front.views.RegisterView import RegisterView
from front.views.page_view import HomePageView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('register', RegisterView.as_view()),
]
