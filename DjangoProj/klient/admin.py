from django.contrib import admin
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django import forms
from klient.models import Klient, Telefon, Email
from django.contrib import messages

# def checkDlugoscPesel(pesel):
#     return pesel >= 10000000000 and pesel < 100000000000

# def checkCyfreKontrolna(pesel):
#         wagiCyfr = [9, 7, 3, 1, 9, 7, 4, 1, 9, 7]
#         stringPesel = str(pesel)
#         suma = 0
#         licznik = 0
#         for i in stringPesel[:10]:
#             suma += wagiCyfr[licznik] * int(i)
#             licznik += 1
#         cyfraKontrolna = stringPesel[0]
#
#         return cyfraKontrolna == suma % 10

class KlientAdmin(admin.ModelAdmin):
    # form = KlientForm
    list_display = ('imie', 'nazwisko')
    # list_filter = ('nazwisko','imie')
    # def save_model(self, request, obj, form, change):
    #     pesel = form.changed_data.index('pesel')
    #     # if not checkDlugoscPesel(pesel):
    #     #     messages.error(request, 'Zla dlugosc numeru pesel!')
    #     if not checkCyfreKontrolna(pesel):
    #         messages.error(request, 'Zly numer pesel!')


class TelefonAdmin(admin.ModelAdmin):
    list_display = ('numer_telefonu',)
    # list_filter = ('id_klienta','numer_telefonu')

class EmailAdmin(admin.ModelAdmin):
    # list_filter = ('email',)
    list_display = ('email',)

admin.site.register(Klient, KlientAdmin)
admin.site.register(Telefon, TelefonAdmin)
admin.site.register(Email, EmailAdmin)
# Register your models here.
