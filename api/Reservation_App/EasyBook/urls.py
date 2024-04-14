from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import *

app_name = 'EasyBook'

urlpatterns = [
    
    path('', RestaurantListView.as_view(), name='home_data_api'),
    path('restaurant/<int:restaurant_id>/', RestaurantDetailView.as_view(), name='restaurant_detail'),

    path('search/', SearchRestaurantsAPIView.as_view(), name='search_restaurants'),
    
    path('profile/', DiningProfileAPIView.as_view(), name='dining-profile'),
    path('recommendations/', RecommendationAPIView.as_view(), name='recommendations'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
