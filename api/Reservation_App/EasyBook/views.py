from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Restaurant, MenuItem
from django.views.decorators.http import require_http_methods
from django.core import serializers

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
