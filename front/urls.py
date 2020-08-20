from django.urls import path
from front.views.RegisterView import RegisterView
from front.views.page_view import HomePageView
from front.views.thread_view import ThreadView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('thread/create', ThreadView.as_view()),
    path('register', RegisterView.as_view()),
]
