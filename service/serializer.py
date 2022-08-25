from dataclasses import field
from .models import ServiceDetails
from rest_framework import serializers

class ServiceSerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceDetails
        fields = '__all__'


