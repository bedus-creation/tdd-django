from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model


class RegisterTest(TestCase):

    def test_guest_can_access_register_form(self):
        c = Client()
        response = c.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_guest_can_register_into_the_system(self):
        data = {
            'email': 'tmgbedu@gmail.com',
            'password': 'password',
            'name': 'Bedram Tamang'
        }
        self.client.post('/register', data)

        # Assert Database has users
        User = get_user_model()
        self.assertEqual(User.objects.get(), 1)
