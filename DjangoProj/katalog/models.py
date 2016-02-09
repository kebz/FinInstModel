from django.db import models
from globalnewartosci.models import *
from django.utils.translation import ugettext_lazy as _


class Usluga(models.Model):
    id_uslugi= models.CharField( primary_key=True, max_length=50, default="US")
    typ_uslugi = models.ForeignKey('globalnewartosci.TypUslugi', to_field='typ_uslugi', db_column='typ_uslugi')

    class Meta:
        app_label = 'katalog'
        verbose_name_plural = 'uslugi'
        ordering = ['typ_uslugi']

class Oprocentowanie(models.Model):
    oprocentowanie=models.FloatField( default=0.0 )
    id_uslugi=models.ForeignKey('Usluga', to_field='id_uslugi', db_column='id_uslugi', primary_key=True, on_delete=models.CASCADE)
    st_rynkowa=models.ForeignKey('globalnewartosci.Stopa_rynkowa', to_field='st_rynkowa')

    class Meta:
        app_label = 'katalog'
        verbose_name_plural = 'oprocentowanie'
        ordering = ['id_uslugi']

class Wartosc(models.Model):
    wartosc_t=models.FloatField( default=0.0 )
    wartosc_0=models.FloatField( default=0.0 )
    id_uslugi=models.ForeignKey('Usluga', to_field='id_uslugi', db_column='id_uslugi', primary_key=True, on_delete=models.CASCADE )

    class Meta:
        app_label = 'katalog'
        verbose_name_plural = 'wartosci'
        ordering = ['id_uslugi']
