from rest_framework import serializers
from .models import *

class VehiculoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehiculos
        fields = '__all__' #serializa todos los campos del modelo