from rest_framework import serializers
from .models import *

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('__all__')

class DistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distance
        fields = ('__all__')
    