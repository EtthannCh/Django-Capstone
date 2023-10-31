from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Menu,Booking
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, MenuItemSerializer, BookingSerializer
# Create your views here.
def index(request):
    return render(request, "index.html", {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
@api_view()
@permission_classes([IsAuthenticated])    
def msg(request):
    return Response({"message" : "this view is protected"})