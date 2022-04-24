from django.urls import path
from front.views.register import Register
from front.views.page_view import HomePageView
from front.views.thread_view import ThreadView
from front.views.login import Login

urlpatterns = [
    path('', HomePageView.as_view()),
    path('thread/create', ThreadView.as_view()),
    path('register', Register.as_view()),

    path('login', Login.as_view()),
]
