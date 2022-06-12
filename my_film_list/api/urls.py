from django.urls import path, include
from my_film_list.serializers.ObraCinematograficaSerializer import ObraCinematograficaSerializer
from rest_framework import routers
from .rest_framework_views import ObraCinematograficaViewSet

router = routers.DefaultRouter()
router.register(r'obras-cinematograficas', ObraCinematograficaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
