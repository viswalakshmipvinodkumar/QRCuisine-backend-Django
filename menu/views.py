from rest_framework import generics
from .models import MenuItem, QRCode
from .serializers import MenuItemSerializer, QRCodeSerializer

class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class QRCodeDetailView(generics.RetrieveAPIView):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer
