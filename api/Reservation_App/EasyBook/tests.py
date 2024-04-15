from django.test import TestCase
from django.contrib.auth.models import User

from .models import *
from .utils import *


# python manage.py test EasyBook.tests.RecommendationSystemTest
class RecommendationSystemTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        users = [
            {'username': 'alice', 'password': 'testpassword123'},
            {'username': 'bob', 'password': 'testpassword456'}
        ]
        for user_data in users:
            User.objects.create_user(**user_data)

        cls.restaurant1 = Restaurant.objects.create(name='The Cozy Pasta', location='1234 Elm Street', cuisine_type='Italian', health_rating=4.5, price_level=2)
        cls.restaurant2 = Restaurant.objects.create(name='Sushi Place', location='2345 Oak Avenue', cuisine_type='Japanese', health_rating=4.7, price_level=3)
        cls.restaurant3 = Restaurant.objects.create(name='The Burger Joint', location='3456 Pine Street', cuisine_type='American', health_rating=4.2, price_level=1)

        Review.objects.create(user=User.objects.get(username='alice'), restaurant=cls.restaurant1, rating=5, comment='Loved it!')
        Review.objects.create(user=User.objects.get(username='alice'), restaurant=cls.restaurant2, rating=4, comment='Pretty good sushi.')
        Review.objects.create(user=User.objects.get(username='bob'), restaurant=cls.restaurant3, rating=5, comment='Best burgers ever!')

    def test_collaborative_filtering_recommendations(self):
        user = User.objects.get(username='alice')
        recommended_restaurants = get_collaborative_filtering_recommendations(user)
        self.assertIn(self.restaurant3.id, recommended_restaurants)

    def test_content_based_recommendations(self):
        user_profile = DiningProfile.objects.get(user__username='alice')
        all_restaurants = Restaurant.objects.all()
        recommended_restaurants = get_content_based_recommendations(user_profile, all_restaurants)
        recommended_names = [restaurant.name for restaurant in recommended_restaurants]
        self.assertIn('The Cozy Pasta', recommended_names)