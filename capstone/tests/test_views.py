from django.test import TestCase
from django.urls import reverse
from restaurant.models import menu
import json
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuViewTest(APITestCase):
    def setUp(self):
        # Create a user and obtain a token
        self.user = User.objects.create_user(username="testuser1", password="testpassword1")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        #Create test instances
        menu.objects.create(title="Item1", price=10.99, inventory=50)
        menu.objects.create(title="Item2", price=15.99, inventory=30)
        menu.objects.create(title="Item3", price=8.49, inventory=20)

    def test_getall(self):
        url = reverse('menu-items')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.content)
        self.assertEqual(len(data), 3)