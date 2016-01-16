from django.db import models
from katalog.models import *
from django.utils import timezone

class Platnosc(models.Model):
     id_uslugi=models.ForeignKey('katalog.Usluga', to_field='katalog.Usluga.id_uslugi', on_delete=models.CASCADE)
     wartosc=models.FloatField( default=0.0 )
     czestotliwosc=models.IntegerField(default=1)           #ile razy w roku platnosc
     dlugosc=models.FloatField(null=True)                   #jak długo (w latach)

class Historia_platnosci(models.Model):
    id_uslugi=models.ForeignKey('katalog.Usluga', to_field='katalog.Usluga.id_uslugi', on_delete=models.CASCADE)
    kwota=models.FloatField( default=0.0 )
    data=models.DateTimeField (default=timezone.now)

# Create your models here.
