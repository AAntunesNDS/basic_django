from django.utils.translation import gettext_lazy as _
from django.db import models


class StreamingService(models.Model):
    name = models.CharField(max_length=200)
    has_service = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class ObraCinematografica(models.Model):
    class StatusObraCinematografica(models.TextChoices):
        INACABADO = 'IN', _('Inacabado')
        NOVO = 'NO', _('Novo')
        REASSISTIR = 'RE', _('Reassistir')

    class TypeObraCinematografica(models.TextChoices):
        FILME = 'FI', _('Filme')
        SERIADO = 'SE', _('Seriado')
        
    status_obra_cinematografica = models.CharField(
        max_length=10,
        choices=StatusObraCinematografica.choices,
        default=StatusObraCinematografica.NOVO,
    )

    type_obra_cinematografica = models.CharField(
        max_length=7,
        choices=TypeObraCinematografica.choices,
        default=TypeObraCinematografica.SERIADO,
    )

    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    streaming_service = models.ForeignKey(StreamingService, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name
