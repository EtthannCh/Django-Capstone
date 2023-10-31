from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from rest_framework.test import APIClient
from restaurant.serializers import MenuItemSerializer
class MenuViewSet(TestCase):
    def setup(self):
        self.client = APIClient()
        Menu.objects.create(title = "item1", price=120, inventory=50)
        Menu.objects.create(title = "item2", price=20, inventory=30)
    
    def test_getall(self):
        url = reverse("menu-item")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        menu_items = Menu.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)