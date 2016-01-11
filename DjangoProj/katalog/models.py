from django.db import models
from django.utils.translation import ugettext_lazy as _


class Kategoria(models.Model):
    nazwa = models.CharField(_("Nazwa"), max_length=50)
    nadKategoria = models.ForeignKey("self", verbose_name=_(u"Nad kategoria"), blank=True, null=True)   #TODO: Zmienic to "Nad kategoria na cos co normalnie brzmi"


class Produkt(models.Model):
    nazwa = models.CharField(_("Nazwa"), max_length=80, blank=True)
    cena = models.FloatField(_("Cena"), default=0.0)
# Create your models here.
