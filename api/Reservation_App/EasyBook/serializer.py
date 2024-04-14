from rest_framework import serializers 
from .models import *
  
class RestaurantSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Restaurant 
        fields = ['name', 'detail'] 
        
class DiningProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningProfile
        fields = ['preferences', 'allergies', 'favorite_cuisines', 'desired_dining_experiences']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'restaurant', 'rating', 'comment', 'created_at']