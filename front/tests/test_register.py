from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from front.forms.UserRegistrationForm import UserRegistrationForm


class RegisterTest(TestCase):

    def test_guest_can_access_register_form(self):
        c = Client()
        response = c.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_form_is_valid_for_given_data(self):
        data = {
            'email': 'tmgbedu@gmail.com',
            'password1': '#bedu123TamanG',
            'password2': '#bedu123TamanG',
        }
        form = UserRegistrationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_guest_can_register_into_the_system(self):
        data = {
            'email': 'tmgbedu@gmail.com',
            'password1': '#bedu123TamanG',
            'password2': '#bedu123TamanG',
        }
        response = self.client.post('/register', data, follow=True)
        self.assertTrue(
            ['success' in m.tags for m in list(response.context['messages'])])

        # Assert Database has users
        User = get_user_model()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().email, data['email'])
