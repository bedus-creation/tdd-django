from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import auth
from .factories.UserFactory import UserFactory


class LoginTest(TestCase):
    http = Client()

    def test_guest_can_access_login_page(self):
        response = self.http.get('/login')

        self.assertEqual(response.status_code, 200)

    def test_user_can_login_with_username_and_password(self):
        user = UserFactory(
            email="test@gmail.com"
        )

        response = self.http.post('/login', {
            "email": user.email,
            "password": user.password
        })

        self.assertTrue(user.is_authenticated)
        self.assertRedirects(response, '/')
