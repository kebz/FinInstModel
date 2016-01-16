from django.db import models

class TypUslugi(models.Model):
    typ_uslugi = models.CharField(primary_key=True, max_length=80)

class Stopa_rynkowa(models.Model):
    st_rynkowa=models.FloatField(primary_key=True)

# Create your models here.
