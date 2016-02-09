from django.db import models
from katalog.models import Usluga
from klient.models import Klient


class Portfel(models.Model):
    id_portfela=models.CharField( primary_key=True, max_length=50, default="PR")
    wartosc=models.BigIntegerField(default=None)
    id_klienta=models.ForeignKey('klient.Klient', to_field='id_klienta', db_column='id_klienta')

    class Meta:
        app_label = 'portfel'
        verbose_name_plural = 'portfele'

class Elementy_portfela(models.Model):
    id_portfela= models.ForeignKey('Portfel',to_field='id_portfela', db_column='id_portfela', on_delete=models.CASCADE)
    id_uslugi=models.ForeignKey('katalog.Usluga',to_field='id_uslugi', db_column='id_uslugi', on_delete=models.CASCADE)

    class Meta:
        app_label = 'portfel'
        verbose_name_plural = 'elementy portfeli'
        unique_together = ('id_portfela', 'id_uslugi')
