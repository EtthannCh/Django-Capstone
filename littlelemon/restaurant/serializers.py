from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id","title", "price", "inventory"]
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
    
    def create(self, validate_data):
        user = User.objects.create_user(
            username = validate_data["username"],
            email = validate_data["email"],
            password= validate_data["password"],
        )
        return user