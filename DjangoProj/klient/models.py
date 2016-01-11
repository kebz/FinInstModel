from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Klient(models.Model):
    uzytkownik = models.ForeignKey(User, blank=True, null=True)
    pesel = models.IntegerField()
    def get_email_address(self):
        if self.uzytkownik:
            return self.uzytkownik.email
        else:
            return None
    class Meta:
        app_label = 'klient'

class Kontakt:
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    numer_telefonu = models.IntegerField()
    numer = models.IntegerField()
    ulica = models.CharField(_("Ulica"), max_length=50)
    miasto = models.CharField(_("Miasto"), max_length=50)
    kod_pocztowy = models.CharField(_("Kod pocztowy"), max_length=6)
    panstwo = models.CharField(_("Panstwo"), max_length=50)

    # company_name = models.CharField(_("Company name"), max_length=50, blank=True, null=True)
    # phone = models.CharField(_("Phone"), blank=True, null=True, max_length=20)
    # email = models.EmailField(_("E-Mail"), blank=True, null=True)

    def __unicode__(self):
        return u'%s %s (%s)' % (self.klient.user.first_name, self.klient.user.last_name)

    class Meta:
        app_label = 'klient'
# Create your models here.
