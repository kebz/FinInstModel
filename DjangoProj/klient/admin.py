from django.contrib import admin
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django import forms
from klient.models import Klient, Telefon, Email
from django.contrib import messages

class KlientAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko')


class TelefonAdmin(admin.ModelAdmin):
    list_display = ('numer_telefonu',)
    fields = ('numer_telefonu', 'id_klienta')

class EmailAdmin(admin.ModelAdmin):
    list_display = ('email',)
    fields = ('email', 'id_klienta')

admin.site.register(Klient, KlientAdmin)
admin.site.register(Telefon, TelefonAdmin)
admin.site.register(Email, EmailAdmin)
# Register your models here.
