from unicodedata import name
from django.test import TestCase
from my_film_list.models import StreamingService, ObraCinematografica

import datetime

class StreamingServiceTestCase(TestCase):
    def setUp(self):
        StreamingService.objects.create(name="Prime Video")

    def test_streaming_service_can_create(self):
        prime_video = StreamingService.objects.create(name="Prime Video")
        self.assertEqual(prime_video.name, 'Prime Video')

class ObraCinematograficaTestCase(TestCase):

    def setUp(self):
        prime_video = StreamingService.objects.create(name="Prime Video")
        ObraCinematografica.objects.create(name="Green Book", pub_date="2019-10-25", streaming_service=prime_video)

    def test_filme_can_create(self):
        prime_video = StreamingService.objects.create(name="Prime Video")
        green_book = ObraCinematografica.objects.create(name="Green Book", pub_date="2019-10-25", streaming_service=prime_video)
        self.assertEqual(green_book.name, 'Green Book')

    def test_seriado_can_create(self):
        prime_video = StreamingService.objects.create(name="Prime Video")
        green_book = ObraCinematografica.objects.create(name="Dr House", pub_date="2019-10-25", streaming_service=prime_video)
        self.assertEqual(green_book.name, 'Dr House')
