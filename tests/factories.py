"""This unit contains Factory classes to work with database during testing"""
import factory
from ads.models import Ads, Category
from users.models import User
# --------------------------------------------------------------------------


class UserFactory(factory.django.DjangoModelFactory):
    """UserFactory serves to add users to the database for testing purposes"""
    class Meta:
        model = User

    username = factory.Faker('name')
    password = 'test user'
    birth_date = '2010-01-01'


class CategoryFactory(factory.django.DjangoModelFactory):
    """CategoryFactory serves to add new categories to the database"""
    class Meta:
        model = Category

    slug = factory.Faker('slug')
    name = 'test category'


class AdsFactory(factory.django.DjangoModelFactory):
    """This class creates a fake advertisements using UserFactory and
    CategoryFactory"""
    class Meta:
        model = Ads
    name = 'Дубовый шкаф'
    price = 240
    is_published = False
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
