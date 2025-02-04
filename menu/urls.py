from django.urls import path
from .views import MenuItemListCreateView, QRCodeDetailView ,LoginView

urlpatterns = [
    path('menu/', MenuItemListCreateView.as_view(), name='menu-list'),
    path('qrcode/<int:pk>/', QRCodeDetailView.as_view(), name='qrcode-detail'),
     path('login/', LoginView.as_view(), name='login'),
]


