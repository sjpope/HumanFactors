from django.urls import path
from .views import *

app_name = 'EasyBook'

urlpatterns = [
    path('home/', home_data_api_view, name='home_data_api'),
    path('results/', results_data_api_view, name='results_data_api'),
]
