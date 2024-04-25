from django.test import TestCase
from django.contrib.auth.models import User

from .models import *
from .utils import *

# Run this script inside Django's shell
# python manage.py shell

from EasyBook.models import Restaurant, Review, MenuItem
from django.contrib.auth.models import User

# Create Restaurants
r1 = Restaurant.objects.create(name='The Gourmet Hut', address='123 Fancy St, Gourmet City', location='Downtown', latitude=34.052235, longitude=-118.243683, cuisine_type='French', health_rating=9.0, price_level=3)
r2 = Restaurant.objects.create(name='Sushi Palace', address='321 Sushi Blvd, Fish Town', location='Uptown', latitude=35.689487, longitude=139.691711, cuisine_type='Japanese', health_rating=8.5, price_level=4)
r3 = Restaurant.objects.create(name='Pizza Planet', address='404 Pie Lane, Cheesy Town', location='Suburbs', latitude=40.712776, longitude=-74.005974, cuisine_type='Italian', health_rating=7.5, price_level=2)

# Assume User ID 1 exists
user = User.objects.create(id=1, username='testuser', password='testpassword123')

# Create Reviews
Review.objects.create(user=user, restaurant=r1, rating=5, comment='Absolutely fantastic!')
Review.objects.create(user=user, restaurant=r2, rating=4, comment='Great sushi, but a bit pricey.')
Review.objects.create(user=user, restaurant=r3, rating=3, comment='Decent pizza, good for quick meals.')

# Create Menu Items
MenuItem.objects.create(restaurant=r1, name='Foie Gras', description='Delicate duck liver with a hint of brandy.', price=25.00)
MenuItem.objects.create(restaurant=r2, name='California Roll', description='Crab stick, avocado, and cucumber.', price=12.50)
MenuItem.objects.create(restaurant=r3, name='Pepperoni Pizza', description='Classic pepperoni with mozzarella cheese.', price=15.00)

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