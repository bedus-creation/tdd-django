from django.test import TestCase
from django.test import Client


class ThreadTest(TestCase):
    http = Client()

    def test_user_can_access_thread_post_form(self):
        response = self.http.get('/thread/create')

        self.assertEqual(response.status_code, 200)
