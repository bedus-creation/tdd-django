from django.urls import include, path, re_path
from App import views

urlpatterns = [
    re_path(r'^$', views.Index, name='index'),
    path('blog/<int:pk>/<str:slug>',
         views.BloglDetailView.as_view(), name='blog'),
]
