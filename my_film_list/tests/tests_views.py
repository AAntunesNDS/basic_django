from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK

class ObraCinematograficaViewSet(APITestCase):
    base_url = "/my_film_list/api-rest/"
    
    def test_get_obras_cinematograficas(self):
        response = self.client.get(f'{self.base_url}obras-cinematograficas/')
        assert(response.status_code == HTTP_200_OK)