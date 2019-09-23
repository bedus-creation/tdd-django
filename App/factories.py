import factory
from . import models


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Blog

    title = "this is ok"
    content = "okasdjf aksdfn"
