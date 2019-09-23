from django.db import models
from django.utils.text import slugify
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def link(self):
        return '/blog/' + str(self.id) + '/' + slugify(self.title, allow_unicode=True)

    def __str__(self):
        return self.title + " : " + self.content


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
