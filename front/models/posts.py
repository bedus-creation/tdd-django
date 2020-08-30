from django.db import models
from django.utils.text import slugify
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=100,
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
