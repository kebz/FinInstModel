from django.test import TestCase
from klient.models import *

class KlientTestCase(TestCase):
    def test_klienta(self):
        u1 = User.objects.create(username="kebz", first_name="piotr", last_name="chabinka")
        k1 = Klient.objects.create(uzytkownik=u1, pesel = 0000000000)
        piotr = Klient.objects.get(uzytkownik = u1)


# Create your tests here.
