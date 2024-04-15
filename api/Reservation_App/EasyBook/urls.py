from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
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
    
    path('api/register/', RegisterView.as_view(), name='api_register'),
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
]
