from django.urls import path
from . import views

urlpatterns = [
    path('api/home/', views.home_data_api_view, name='home_data_api'),
    path('api/results/', views.results_data_api_view, name='results_data_api'),
]
