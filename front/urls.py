from django.urls import path
from front.views.RegisterView import RegisterView

urlpatterns = [
    path('register', RegisterView.as_view()),
]
