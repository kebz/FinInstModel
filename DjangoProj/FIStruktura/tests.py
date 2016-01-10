from django.test import TestCase
from FIStruktura.models import *

class KlientTestCase(TestCase):
    def test_klienta(self):
        k1 = Klient.objects.create(imie="piotr", nazwisko="chabinka", pesel=0000000000, adres = "adres")
        piotr = Klient.objects.get(imie = "piotr")
        kontakt = Kontakt.objects.create(klient=piotr, kontakt="przyklad@przyklad.com")


# Create your tests here.
