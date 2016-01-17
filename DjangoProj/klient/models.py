from django.db import models

class Klient(models.Model):
    id_klienta= models.CharField( primary_key=True, null=False, max_length=500, default="KL")
    imie = models.CharField( max_length=50, default=None)
    nazwisko = models.CharField(max_length=50, default=None)
    pesel = models.BigIntegerField(unique=True, default=None)

    class Meta:
        app_label = 'klient'

class Kontakt(models.Model):
    id_klienta = models.ForeignKey('Klient',to_field='id_klienta', on_delete=models.CASCADE)
    numer_telefonu = models.BigIntegerField(default=None)
    numer = models.CharField( max_length=50, default=None)
    ulica = models.CharField( max_length=50, default=None)
    miasto = models.CharField( max_length=50, default=None)
    kod_pocztowy = models.CharField( max_length=6, default=None)
    panstwo = models.CharField( max_length=50, default=None)

    class Meta:
       app_label = 'klient'

