
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=True)),  # Non-API redirect
    # path('home/', include('your_non_api_app.urls')),  # For non-API routes
    path('accounts/', include('allauth.urls')),  # Authentication views for Django Allauth
    path('api/', include('EasyBook.urls', namespace='EasyBook')),  # Direct API access
]
