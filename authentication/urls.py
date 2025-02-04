from django.urls import path
from .views import RestaurantRegisterView, ChefRegisterView

urlpatterns = [
    path('register/restaurant/', RestaurantRegisterView.as_view(), name='register-restaurant'),
    path('register/chef/', ChefRegisterView.as_view(), name='register-chef'),
    
    
]
