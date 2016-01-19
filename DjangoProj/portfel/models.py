from django.db import models
from globalnewartosci.models import *
from klient.models import *


class Portfel(model.Model):
    id_portfela=models.CharField(models.CharField( primary_key=True, null=False, max_length=500, default="PR"))
    id_klienta=models.ForeignKey('Klient',to_field='id_klienta',on_delete=model.CASCADE)
    wartosc=model.BigIntegerField(default=None)

class Elementy_portfela(model.Model):
    id_portfela= models.ForeignKey('Portfel',to_field='id_portfela', on_delete=model.CASCADE)
    id_uslugi=models.ForeignKey('katalog.Usluga',to_field='id_uslugi', on_delete=model.CASCADE)
    ilosc=model.BigIntegerField(default=None)
