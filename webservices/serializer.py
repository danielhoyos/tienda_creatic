from rest_framework import serializers
from home.models import *

class producto_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url', 'id', 'nombre', 'status', 'picture', 'precio', 'stock', 'marca', 'categoria') 

class marca_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ('url', 'id', 'nombre')

class categoria_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'nombre')