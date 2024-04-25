
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='home/', permanent=True)),  
    path('home/', include('EasyBook.urls', namespace='EasyBook')),  
    path('accounts/', include('allauth.urls')),

]
