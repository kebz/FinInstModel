from django.db import models


# class KlientManager(models.Manager):
#     def stworz_klienta(self, imie, nazwisko, pesel, adres):
#         klient = self.create(imie=imie, nazwisko=nazwisko, pesel=pesel, adres=adres)
#         return klient


class Klient(models.Model):
    # id = models.IntegerField(primary_key=True)
    imie = models.CharField(max_length=20, null=True)  # trzeba zmienic zeby nie moglo byc null
    nazwisko = models.CharField(max_length=20, null=True)  # trzeba zmienic zeby nie moglo byc null
    pesel = models.IntegerField(unique=True, null=True)  # trzeba zmienic zeby nie moglo byc null
    adres = models.CharField(max_length=100, null=True)  # trzeba zmienic zeby nie moglo byc null
    # object = KlientManager()


class Kontakt(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    kontakt = models.CharField(max_length=50, null=True)

# Create your models here.
