from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.db.models import Q

from .models import *
from .serializer import *
from .utils import *

from rest_framework import generics
from rest_framework.views import APIView 
from rest_framework.response import Response 

class RecommendationAPIView(APIView):
    def get(self, request, format=None):
        recommendations = get_recommendations(request.user)
        # Format recommendations as needed, potentially using a serializer
        return Response(recommendations)
    
class DiningProfileAPIView(generics.RetrieveUpdateAPIView):
    queryset = DiningProfile.objects.all()
    serializer_class = DiningProfileSerializer

    def get_object(self):
        # Assuming you have a one-to-one relationship to the user
        return self.queryset.get(user=self.request.user)
class RestaurantView(APIView): 
    
    serializer_class = RestaurantSerializer 
  
    def get(self, request): 
        detail = [ {"name": detail.name,"detail": detail.detail}  
        for detail in Restaurant.objects.all()] 
        return Response(detail) 
  
    def post(self, request): 
  
        serializer = RestaurantSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data) 
        
        
def search_restaurants(request):
    
    # Get Q Param from URL, can be name or address
    query = request.GET.get('q', None)  
    
    if query is not None:
        restaurants = Restaurant.objects.filter(
            Q(address__icontains=query) | Q(name__icontains=query)      
        )
    else:
        restaurants = Restaurant.objects.all()
    
    data = {'restaurants': list(restaurants.values())}  
    return JsonResponse(data)

   
# def home_data_api_view(request):
#     # query models, send to frontend
#     restaurants = Restaurant.objects.all()  
#     data = {
#         'message': 'Placeholder data for home page',
#         'restaurants': list(restaurants.values())  # creates list of dictionaries, [{'x': 1}, {'y': 2]
#     }
#     return JsonResponse(data)

def results_data_api_view(request):
    # Passing filters in q params here
    search_query = request.GET.get('search', '')
    filter_results = MenuItem.objects.filter(name__icontains=search_query)  
    data = {
        'message': 'Placeholder data for results page',
        'results': list(filter_results.values())
    }
    return JsonResponse(data)

@require_http_methods(["GET"])
def home_data_api_view(request):
    # Fetch all restaurants or apply filters if any (e.g., based on query parameters)
    restaurants = Restaurant.objects.all()
    # Serialize the queryset to JSON
    data = serializers.serialize('json', restaurants)
    return HttpResponse(data, content_type="application/json")

@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def restaurant_detail_api_view(request, restaurant_id):
    if request.method == 'GET':
        # Retrieve a restaurant by id
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
            data = serializers.serialize('json', [restaurant])
            return HttpResponse(data, content_type="application/json")
        except Restaurant.DoesNotExist:
            return JsonResponse({'message': 'Restaurant not found'}, status=404)

    elif request.method == 'POST':
        
        # TO-DO: Create a new restaurant entry and parse request body to get the restaurant data
        
        pass

    elif request.method == 'PUT':
        
        # TO-DO: Create logic to update an existing restaurant
        
        pass

    elif request.method == 'DELETE':
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
            restaurant.delete()
            return JsonResponse({'message': 'Restaurant deleted'}, status=204)
        except Restaurant.DoesNotExist:
            return JsonResponse({'message': 'Restaurant not found'}, status=404)
        
def filtered_restaurants(request):
    queryset = Restaurant.objects.all()
    cuisine = request.GET.get('cuisine')
    if cuisine:
        queryset = queryset.filter(cuisine_type=cuisine)
    # will need more filters here
    data = serializers.serialize('json', queryset)
    return HttpResponse(data, content_type='application/json')
