from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django import forms
from django.utils.text import slugify
from django.contrib import messages
import logging

logr = logging.getLogger(__name__)


class Klient(models.Model):
    id_klienta = models.CharField(primary_key=True, null=False, max_length=50, default="KL")
    imie = models.CharField(max_length=50, default=None)
    nazwisko = models.CharField(max_length=50, default=None)
    pesel = models.BigIntegerField(unique=True)
    adres = models.CharField(max_length=250, default=None)

    # def checkDlugoscPesel(self):
    #     return self.pesel >= 10000000000 and self.pesel < 10000000000

    # def checkCyfreKontrolna(pesel):
    #     wagiCyfr = [9, 7, 3, 1, 9, 7, 4, 1, 9, 7]
    #     stringPesel = str(pesel)
    #     suma = 0
    #     for i in stringPesel[:10]:
    #         suma += wagiCyfr[i] * i
    #     cyfraKontrolna = stringPesel[10]

        # return cyfraKontrolna == suma % 10
    # def pre_save(self, *args, **kwargs):
    #     if(self.checkDlugoscPesel()):
    #         super(Klient, self).save(*args, **kwargs)
    #     else:
    #         messages.add_message(request, messages.INFO, 'Car has been sold')

    def __unicode__(self):
        return u'%s %s' % (self.imie, self.nazwisko)

    class Meta:
        app_label = 'klient'
        verbose_name_plural = 'klienci'
        ordering = ['nazwisko']

# # @staticmethod
# def checkDlugoscPesel(pesel):
#     return pesel >= 10000000000 and pesel < 10000000000
#
#
# @receiver(pre_save, sender=Klient)
# def checkKlientPesel(sender, instance, *args, **kwargs):
#     # imie = instance.imie
#     pesel = instance.pesel
#     # if checkDlugoscPesel(pesel):
#     # strPesel = slugify(instance.pesel)
#     # strPesel = strPesel.strip('-')
#     # pesel = int(strPesel)
#     # if instance.checkDlugoscPesel():
#         # pass
#     raise forms.ValidationError(('Pesel: %(value)s jest za krotki '),
#                                 code='invalid',
#                                 params={'value': pesel}, )
#         # response = HttpsResponse('', kwargs.get('instance').pesel)
#
#
# pre_save.connect(checkKlientPesel)







# @receiver(pre_save, sender=Klient)
# def checkKlientPesel(sender, instance, *args, **kwargs):
#     pesel = slugif(instance.pesel)
#     if checkDlugoscPesel(pesel):
#         raise forms.ValidationError(('Pesel: %(value)s jest za krotki '),
#                                     code='invalid',
#                                     params={'value': 'pesel'}, )
        # response = HttpsResponse('', kwargs.get('instance').pesel)


# pre_save.connect(checkKlientPesel)


class Telefon(models.Model):
    id_klienta = models.ForeignKey('Klient', to_field='id_klienta', db_column='id_klienta', primary_key=True,
                                   on_delete=models.CASCADE)
    numer_telefonu = models.BigIntegerField(default=None)

    class Meta:
        app_label = 'klient'
        verbose_name_plural = 'telefony'
        ordering = ['id_klienta']
        unique_together = ('id_klienta', 'numer_telefonu')

    def __unicode__(self):
        return u'%s' % (self.numer_telefonu)


class Email(models.Model):
    id_klienta = models.ForeignKey('Klient', to_field='id_klienta', db_column='id_klienta', primary_key=True,
                                   on_delete=models.CASCADE)
    email = models.CharField(max_length=50, default=None)

    class Meta:
        app_label = 'klient'
        verbose_name_plural = 'e-mail'
        ordering = ['id_klienta']
        unique_together = ('id_klienta', 'email')

    def __unicode__(self):
        return u'%s' % (self.email)
