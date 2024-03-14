from rest_framework import serializers
from .models import DetalleSolicitudCompra, SolicitudCompra

class SolicitudCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudCompra
        fields = '__all__'

class DetalleSolicitudCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleSolicitudCompra
        fields = '__all__'