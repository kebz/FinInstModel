from django.db import models

class Klient(models.Model):
    id_klienta= models.CharField( primary_key=True, null=False, max_length=500, default="KL")
    imie = models.CharField( max_length=50, default=None)
    nazwisko = models.CharField(max_length=50, default=None)
    pesel = models.BigIntegerField(unique=True, default=None)
    adres = models.CharField(max_length=500, default=None)

    def __unicode__(self):
        return u'%s %s' % (self.imie, self.nazwisko)

    class Meta:
        app_label = 'klient'
        verbose_name_plural = 'klienci'
        ordering = ['nazwisko']



class Telefon(models.Model):
    id_klienta = models.ForeignKey('Klient',to_field='id_klienta', on_delete=models.CASCADE, primary_key=True)
    numer_telefonu = models.BigIntegerField(default=None)

    class Meta:
        app_label = 'klient'
        verbose_name_plural = 'telefony'
        ordering = ['id_klienta']

    def __unicode__(self):
        return u'%s' % (self.numer_telefonu)

class Email(models.Model):
    id_klienta = models.ForeignKey('Klient',to_field='id_klienta', on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=50, default=None)

    class Meta:
        app_label = 'klient'
        verbose_name_plural = 'e-mail'
        ordering = ['id_klienta']


    def __unicode__(self):
        return u'%s' % (self.email)