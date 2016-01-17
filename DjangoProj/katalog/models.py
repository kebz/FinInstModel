from django.db import models
from globalnewartosci.models import *
from django.utils.translation import ugettext_lazy as _


class Usluga(models.Model):
    id_uslugi= models.CharField( primary_key=True, max_length=500, default="US")
    typ_uslugi = models.ForeignKey('globalnewartosci.TypUslugi', to_field='typ_uslugi',  on_delete=models.CASCADE)

class Oprocentowanie(models.Model):
    id_uslugi=models.ForeignKey('Usluga', to_field='id_uslugi', on_delete=models.CASCADE)
    oprocentowanie=models.FloatField( default=0.0 )
    st_rynkowa=models.ForeignKey('globalnewartosci.Stopa_rynkowa', to_field='st_rynkowa', on_delete=models.CASCADE)

class Wartosc(models.Model):
    id_uslugi=models.ForeignKey('Usluga', to_field='id_uslugi', on_delete=models.CASCADE)
    wartosc_t=models.FloatField( default=0.0 )
    wartosc_0=models.FloatField( default=0.0 )

# from django.db import models
# from django.utils.translation import ugettext_lazy as _
#
#
# class Kategoria(models.Model):
#     nazwa = models.CharField(_("Nazwa"), max_length=50)
#     nadKategoria = models.ForeignKey("self", verbose_name=_(u"Nad kategoria"), blank=True, null=True)   #TODO: Zmienic to "Nad kategoria na cos co normalnie brzmi"
#
#
# class Produkt(models.Model):
#     nazwa = models.CharField(_("Nazwa"), max_length=80, blank=True)
#     cena = models.FloatField(_("Cena"), default=0.0)
# # Create your models here.
