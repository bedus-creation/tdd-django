from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from front.forms.UserRegistrationForm import UserRegistrationForm
from .factories.UserFactory import UserFactory


class RegisterTest(TestCase):

    def test_guest_can_access_register_form(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_form_is_valid_for_given_data(self):
        data = UserFactory.stub().__dict__
        form = UserRegistrationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_guest_can_register_into_the_system(self):
        data = UserFactory.stub().__dict__
        response = self.client.post('/register', data, follow=True)
        self.assertTrue(
            ['success' in m.tags for m in list(response.context['messages'])])

        # Assert Database has users
        User = get_user_model()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().email, data['email'])
        self.assertEqual(User.objects.first().first_name, data['first_name'])
        self.assertEqual(User.objects.first().last_name, data['last_name'])
