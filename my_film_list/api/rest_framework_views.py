from my_film_list.serializers.ObraCinematograficaSerializer import ObraCinematograficaSerializer
from ..models import ObraCinematografica
from rest_framework import viewsets

class ObraCinematograficaViewSet(viewsets.ModelViewSet):
    queryset = ObraCinematografica.objects.all()
    serializer_class = ObraCinematograficaSerializer