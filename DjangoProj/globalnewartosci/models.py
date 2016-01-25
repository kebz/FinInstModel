from django.db import models

class TypUslugi(models.Model):
    typ_uslugi = models.CharField(primary_key=True, max_length=50)

    class Meta:
        app_label='globalnewartosci'
        verbose_name_plural = 'typ uslugi'

class Stopa_rynkowa(models.Model):
    st_rynkowa=models.FloatField(primary_key=True)

    class Meta:
        app_label='globalnewartosci'
        verbose_name_plural = 'stopa rynkowa'
# Create your models here.
