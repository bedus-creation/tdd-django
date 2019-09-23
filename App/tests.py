from django.test import TestCase
from django.test import Client
from . import factories
# Create your tests here.


class ReadTest(TestCase):

    def test_blog_can_read_by_every_one(self):
        c = Client()
        blog = factories.BlogFactory()
        response = c.get(blog.link())
        self.assertEqual(response.status_code, 200)

    def test_blog_can_be_lists(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
