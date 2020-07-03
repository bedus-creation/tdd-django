from django.contrib.auth import get_user_model
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        # django_get_or_create = ('username',)

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password1 = '#bedu123TamanG'
    password2 = '#bedu123TamanG'
