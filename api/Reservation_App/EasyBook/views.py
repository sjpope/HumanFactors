from django.shortcuts import render
from django.http import JsonResponse

def home_data_api_view(request):
    data = {'message': 'Placeholder data for home page'}
    return JsonResponse(data)

def results_data_api_view(request):
    data = {'message': 'Placeholder data for results page'}
    return JsonResponse(data)

