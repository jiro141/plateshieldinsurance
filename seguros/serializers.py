from rest_framework import serializers
from .models import TarjetaSeguroFlorida

class TarjetaSeguroFloridaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarjetaSeguroFlorida
        fields = '__all__'
