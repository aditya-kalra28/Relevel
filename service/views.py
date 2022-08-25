from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializer import ServiceSerialzer
from .models import ServiceDetails

# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceDetails.objects.all()
    serializer_class = ServiceSerialzer
    
