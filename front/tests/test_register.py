from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from front.forms.UserRegistrationForm import UserRegistrationForm
from .factories.UserFactory import UserFactory
import pprint
from .data.register_data import get_registration_form_data


class RegisterTest(TestCase):
    http = Client()

    def test_guest_can_access_register_form(self):
        response = self.http.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_form_is_valid_for_given_data(self):
        form = UserRegistrationForm(data=get_registration_form_data())

        self.assertTrue(form.is_valid())

    def test_guest_can_register_into_the_system(self):
        data = get_registration_form_data()
        response = self.http.post('/register', data, follow=True)

        self.assertTrue(
            ['success' in m.tags for m in list(response.context['messages'])])

        # Assert Database has users
        user = get_user_model()
        self.assertEqual(user.objects.count(), 1)
        self.assertEqual(user.objects.first().email, data['email'])
        self.assertEqual(user.objects.first().first_name, data['first_name'])
        self.assertEqual(user.objects.first().last_name, data['last_name'])
