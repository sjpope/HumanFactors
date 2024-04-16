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

""" User Auth Views """
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
        query = request.query_params.get('q', None)
        if not query:
            return Response({"error": "Query parameter 'q' is missing."}, status=status.HTTP_400_BAD_REQUEST)
        
        restaurants = Restaurant.objects.filter(Q(address__icontains=query) | Q(name__icontains=query))
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

""" Recommendation Views """
class RecommendationAPIView(APIView):
    """
    Get restaurant recommendations for the user.
    """
    def get(self, request):
        recommendations = get_recommendations(request.user)
        return Response(recommendations)

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