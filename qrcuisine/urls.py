from django.contrib import admin
from django.urls import path, include
from qrcuisine.views import home  # Correctly import 'home' view from the main project directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),  # For authentication-related routes
    path('', home, name='home'),  # Root URL that points to the home view
]
