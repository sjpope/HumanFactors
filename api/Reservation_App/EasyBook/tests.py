from django.test import TestCase
from EasyBook.models import *





""" RESTAURANT MOCK DATA """

restaurants_data = [
    
    {'name': 'The Cozy Pasta', 'location': '1234 Elm Street', 'cuisine_type': 'Italian', 'health_rating': 4.5, 'price_level': 2},
    {'name': 'Sushi Place', 'location': '2345 Oak Avenue', 'cuisine_type': 'Japanese', 'health_rating': 4.7, 'price_level': 3},
    {'name': 'The Burger Joint', 'location': '3456 Pine Street', 'cuisine_type': 'American', 'health_rating': 4.2, 'price_level': 1},
    
]

for restaurant_data in restaurants_data:
    restaurant = Restaurant(**restaurant_data)
    restaurant.save()
    
restaurant1 = Restaurant.objects.get(name='The Cozy Pasta')
restaurant2 = Restaurant.objects.get(name='Sushi Place')

""" MENU ITEM MOCK DATA """
menu_items_data = [
    
    {'restaurant': restaurant1, 'name': 'Spaghetti Carbonara', 'description': 'Creamy pasta with pancetta and parmesan', 'price': 12.99},
    {'restaurant': restaurant2, 'name': 'Nigiri Platter', 'description': 'Assorted sushi with fresh fish', 'price': 15.99},
    
]

for item_data in menu_items_data:
    item = MenuItem(**item_data)
    item.save()