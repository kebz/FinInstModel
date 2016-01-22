from django.contrib import admin
from platnosci.models import Platnosc, Historia_platnosci

class PlatnosciAdmin(admin.ModelAdmin):
    list_display = ('wartosc', 'czestotliwosc', 'dlugosc')

class Historia_platnosciAdmin(admin.ModelAdmin):
    list_display = ('data', 'kwota')

admin.site.register(Platnosc, PlatnosciAdmin)
admin.site.register(Historia_platnosci, Historia_platnosciAdmin)
# Register your models here.
