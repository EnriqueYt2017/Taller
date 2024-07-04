from rest_framework import serializers
from .models import *


#LO UTILIZAMOS PARA TRANSFORMAR PYTHON A JSON
class  VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Vehiculo
        fields = '__all__'

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
            model = Producto
            fields = '__all__'