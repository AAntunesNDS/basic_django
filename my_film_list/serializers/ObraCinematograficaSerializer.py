from ..models import ObraCinematografica
from rest_framework import serializers

# Serializers define the API representation.
class ObraCinematograficaSerializer(serializers.Serializer):
    class Meta:
        model = ObraCinematografica
        fields = [
            'status_obra_cinematografica', 
            'type_obra_cinematografica', 
            'name', 
            'pub_date', 
            'streaming_service'
        ]