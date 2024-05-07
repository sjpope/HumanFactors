from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from .views import *

app_name = 'EasyBook'

urlpatterns = [ 
    
    # /api/resturants/
    path('restaurants/', RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurant/<int:restaurant_id>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    
    path('restaurant/<int:restaurant_id>/book/', BookReservationAPIView.as_view(), name='book_reservation'),
    path('restaurant/<int:restaurant_id>/add_review/', AddReviewAPIView.as_view(), name='add-review'),

    path('reservations/upcoming/', UpcomingReservationsAPIView.as_view(), name='upcoming_reservations'),
    
    path('restaurants/search/', FilteredSearchRestaurantsAPIView.as_view(), name='search_restaurants'),
    
    # /api/search/?q=${encodeURIComponent(searchQuery)}
    path('search/', SearchRestaurantsAPIView.as_view(), name='search_restaurants'),
    
    path('profile/', DiningProfileAPIView.as_view(), name='dining-profile'),
    path('profile/<int:pk>/update', UserProfileUpdateAPIView.as_view(), name='update-profile'),


    path('recommendations/', RecommendationAPIView.as_view(), name='recommendations'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
