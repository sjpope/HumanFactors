from django.shortcuts import render
from django.http import JsonResponse
from .models import Restaurant, MenuItem

def home_data_api_view(request):
    
    # query models, send to frontend
    restaurants = Restaurant.objects.all()  
    data = {
        'message': 'Placeholder data for home page',
        'restaurants': list(restaurants.values())  # creates list of dictionaries, [{'x': 1}, {'y': 2]
    }
    return JsonResponse(data)

def results_data_api_view(request):
    # Assume you pass filters via query parameters, for example
    search_query = request.GET.get('search', '')
    filter_results = MenuItem.objects.filter(name__icontains=search_query)  
    data = {
        'message': 'Placeholder data for results page',
        'results': list(filter_results.values())
    }
    return JsonResponse(data)
