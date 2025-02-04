from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny  # To allow public access to the registration views

from .models import Restaurant, Chef
from .serializers import RestaurantSerializer, ChefSerializer, LoginSerializer


# LoginView should handle user login and issue tokens (if needed)
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # For token-based auth, we can issue a token here or handle login logic
            # Example (if you're using Token Authentication)
            # user = serializer.validated_data['user']
            # token = Token.objects.get_or_create(user=user)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Restaurant Register view, open for public use
class RestaurantRegisterView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [AllowAny]  # Allow any user to register a restaurant


# Chef Register view, open for public use
class ChefRegisterView(generics.CreateAPIView):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
    permission_classes = [AllowAny]  # Allow any user to register a chef
