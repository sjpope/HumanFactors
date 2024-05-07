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

class ReservationSlotSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)
    date_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")  # Format datetime as needed

    class Meta:
        model = ReservationSlot
        fields = ['id', 'user', 'restaurant_name', 'date_time']
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'description', 'rating', 'price', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id']