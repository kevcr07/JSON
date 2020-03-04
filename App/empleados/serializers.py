from rest_framework import serializers
from .models import Usuario

#se crea un serializer para transportar los datos a traves de la red
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'