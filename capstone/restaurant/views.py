from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from .serializers import *
from .models import *

def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer