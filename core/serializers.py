from rest_framework import serializers
from .models import *


#LO UTILIZAMOSPARA TRANSFORMAR PYTHON A JSON
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Vehiculo
        fields = '__all__'