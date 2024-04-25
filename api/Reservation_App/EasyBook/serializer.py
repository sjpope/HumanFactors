from rest_framework import serializers 
from .models import *
  

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'dining_preferences']
    
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
        
class DiningProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningProfile
        fields = ['preferences', 'allergies', 'favorite_cuisines', 'desired_dining_experiences']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'restaurant', 'rating', 'comment', 'created_at']