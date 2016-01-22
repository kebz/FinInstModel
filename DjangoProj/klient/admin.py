from django.contrib import admin
from klient.models import Klient, Telefon, Email

class KlientAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko')
    # list_filter = ('nazwisko','imie')

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
