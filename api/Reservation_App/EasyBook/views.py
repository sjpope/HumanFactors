from datetime import timezone
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import *
from .serializer import *
from .utils import *
from .forms import RegisterForm

from rest_framework import generics, status, permissions
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied 
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

import logging
from django.utils.dateparse import parse_datetime
from django_filters import rest_framework as filters

""" User Views """
class UserProfileView(APIView):
    def get(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        logging.error(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Account is not active.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'detail': 'Invalid Credentials or activate account.'}, status=status.HTTP_401_UNAUTHORIZED)
        
class LogoutView(APIView):
    def post(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        form = RegisterForm(request.data)
        if form.is_valid():
            user = form.save()
            return Response({'status': 'success', 'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

""" Restaurant Views """
class RestaurantListView(APIView):
    """
    List all restaurants, or create a new restaurant.
    """
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantDetailView(APIView):
    """
    Retrieve, update or delete a restaurant instance.
    """
    def get_object(self, restaurant_id):
        try:
            return Restaurant.objects.get(id=restaurant_id)
        except Restaurant.DoesNotExist:
            raise NotFound('A restaurant with this ID does not exist.')

    def get(self, request, restaurant_id):
        restaurant = self.get_object(restaurant_id)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    def put(self, request, restaurant_id):
        restaurant = self.get_object(restaurant_id)
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, restaurant_id):
        restaurant = self.get_object(restaurant_id)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SearchRestaurantsAPIView(APIView):
    """
    Search for restaurants by name or address.
    """
    def get(self, request):
        query = request.query_params.get('q')
        price_level = request.query_params.get('price')
        health_rating = request.query_params.get('health')
        cuisine = request.query_params.get('cuisine')
        
        base_query = Restaurant.objects.all()
        
        if query:
            base_query = base_query.filter(Q(name__icontains=query) | Q(address__icontains=query))
        if price_level:
            base_query = base_query.filter(price_level__lte=price_level)
        if health_rating:
            base_query = base_query.filter(health_rating__gte=health_rating)
        if cuisine:
            base_query = base_query.filter(cuisine_type__icontains=cuisine)

        serializer = RestaurantSerializer(base_query, many=True)
        return Response(serializer.data)

class FilteredSearchRestaurantsAPIView(APIView):
    def get(self, request):
        query_params = request.query_params
        base_query = Restaurant.objects.all()

        if 'q' in query_params:
            base_query = base_query.filter(Q(name__icontains=query_params['q']) | Q(address__icontains=query_params['q']))

        if 'price' in query_params:
            base_query = base_query.filter(price_level__lte=query_params['price'])

        if 'health' in query_params:
            base_query = base_query.filter(health_rating__gte=query_params['health'])

        if 'cuisine' in query_params:
            base_query = base_query.filter(cuisine_type__icontains=query_params['cuisine'])

        # Additional filters based on hours of operation, allergies, etc. can be implemented here
        # For hours of operation, you'll need a custom method to parse and match the hours

        serializer = RestaurantSerializer(base_query, many=True)
        return Response(serializer.data)


class RestaurantFilter(filters.FilterSet):
    min_price_level = filters.NumberFilter(field_name="price_level", lookup_expr='gte')
    max_price_level = filters.NumberFilter(field_name="price_level", lookup_expr='lte')
    min_health_rating = filters.NumberFilter(field_name="health_rating", lookup_expr='gte')
    cuisine_type = filters.CharFilter(field_name="cuisine_type", lookup_expr='icontains')

    class Meta:
        model = Restaurant
        fields = ['cuisine_type', 'min_price_level', 'max_price_level', 'min_health_rating']
        
        
""" Reservation Views """
class BookReservationAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, restaurant_id):
        user = request.user
        datetime_str = request.data.get('date_time')
        date_time = parse_datetime(datetime_str)

        if date_time < timezone.now():
            return Response({'error': 'Cannot book a reservation in the past.'}, status=status.HTTP_400_BAD_REQUEST)

        reservation = ReservationSlot(user=user, restaurant_id=restaurant_id, date_time=date_time)
        reservation.save()
        return Response({'status': 'Reservation booked successfully'}, status=status.HTTP_201_CREATED)
    
class UpcomingReservationsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        upcoming_reservations = ReservationSlot.objects.filter(user=user, date_time__gte=timezone.now()).order_by('date_time')
        serializer = ReservationSlotSerializer(upcoming_reservations, many=True)
        return Response(serializer.data)

class ReservationView(APIView):
    """
    Book and view reservations for a restaurant.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, restaurant_id):
        user = request.user
        datetime_str = request.data.get('date_time')
        date_time = parse_datetime(datetime_str)

        reservation = ReservationSlot(user=user, restaurant_id=restaurant_id, date_time=date_time)
        reservation.save()
        return Response({'status': 'Reservation booked'}, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user
        upcoming_reservations = ReservationSlot.objects.filter(user=user, date_time__gte=timezone.now())
        serializer = ReservationSlotSerializer(upcoming_reservations, many=True)
        return Response(serializer.data)
   
""" Review Views """
class AddReviewAPIView(APIView):
    def post(self, request, restaurant_id):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant=restaurant, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
""" Recommendation Views """
class RecommendationAPIView(APIView):
    """
    Get restaurant recommendations for the user.
    """
    def get(self, request):
        user = request.user
        try:
            # Assuming `get_recommendations` handles both collaborative and content-based methods
            recommendations = get_recommendations(user.id)
            return Response({'recommendations': recommendations})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

class DiningProfileAPIView(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a user's dining profile.
    """
    serializer_class = DiningProfileSerializer

    def get_object(self):
        try:
            profile = DiningProfile.objects.get(user=self.request.user)
            self.check_object_permissions(self.request, profile)
            return profile
        except DiningProfile.DoesNotExist:
            raise NotFound('Dining profile not found.')
        except PermissionDenied:
            raise NotFound('You do not have permission to access this profile.')
        
class UserProfileUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        profile, created = UserProfile.objects.get_or_create(user=user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        profile, created = UserProfile.objects.get_or_create(user=user)
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)