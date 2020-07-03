from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
