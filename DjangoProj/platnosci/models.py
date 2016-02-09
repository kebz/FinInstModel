from django.db import models
from katalog.models import *
from django.utils import timezone

class Platnosc(models.Model):
     wartosc=models.FloatField( default=0.0 )
     czestotliwosc=models.IntegerField(default=1)           #ile razy w roku platnosc
     dlugosc=models.FloatField(default=None)                   #jak długo (w latach)
     id_uslugi=models.ForeignKey('katalog.Usluga', to_field='id_uslugi', db_column='id_uslugi', on_delete=models.CASCADE, primary_key=True)
     class Meta:
         app_label='platnosci'
         verbose_name_plural='platnosci'

class Historia_platnosci(models.Model):
    kwota=models.FloatField( default=0.0 )
    data=models.DateTimeField (default=timezone.now)
    id_uslugi=models.ForeignKey('katalog.Usluga', to_field='id_uslugi', db_column='id_uslugi', on_delete=models.CASCADE)

    class Meta:
        app_label='platnosci'
        verbose_name_plural='historie platnosci'
        unique_together = ('id_uslugi', 'data')
# Create your models here.
