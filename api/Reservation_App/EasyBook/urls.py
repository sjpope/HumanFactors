from django.urls import path
from .views import *

app_name = 'EasyBook'

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', home_data_api_view, name='home_data_api'),
    path('results/', results_data_api_view, name='results_data_api'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
