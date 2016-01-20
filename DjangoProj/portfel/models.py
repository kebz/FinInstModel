from django.db import models
from katalog.models import Usluga
from klient.models import Klient


class Portfel(models.Model):
    id_portfela=models.CharField( primary_key=True, null=False, max_length=500, default="PR")
    id_klienta=models.ForeignKey('klient.Klient',to_field='id_klienta',on_delete=models.CASCADE)
    wartosc=models.BigIntegerField(default=None)

class Elementy_portfela(models.Model):
    id_portfela= models.ForeignKey('Portfel',to_field='id_portfela', on_delete=models.CASCADE, primary_key=True)#, max_length=500)
    id_uslugi=models.ForeignKey('katalog.Usluga',to_field='id_uslugi', on_delete=models.CASCADE)
    ilosc=models.BigIntegerField(default=None)
