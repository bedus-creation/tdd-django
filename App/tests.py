from django.test import TestCase
from django.test import Client
# Create your tests here.
class ReadTest(TestCase):

    def test_blog_can_be_lists  (self):
        c = Client()
        response=c.get('/')   
        self.assertEqual(response.status_code,200)
