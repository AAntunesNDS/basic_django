from django.utils.translation import gettext_lazy as _
from django.db import models


class StreamingService(models.Model):
    name = models.CharField(max_length=200)
    has_service = models.BooleanField(default=True)

class Filme(models.Model):
    class FilmeStatus(models.TextChoices):
        INACABADO = 'IN', _('Inacabado')
        NOVO = 'NO', _('Novo')
        REASSISTIR = 'RE', _('Reassistir')

    filme_status = models.CharField(
        max_length=10,
        choices=FilmeStatus.choices,
        default=FilmeStatus.NOVO,
    )
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    streaming_service = models.ForeignKey(StreamingService, on_delete=models.PROTECT)
