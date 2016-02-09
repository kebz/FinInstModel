from django.contrib import admin
from portfel.models import Portfel, Elementy_portfela


from django.contrib import admin
from platnosci.models import Platnosc, Historia_platnosci

class PortfelAdmin(admin.ModelAdmin):
    list_display = ('wartosc', 'id_portfela')

class Elementy_portfelaAdmin(admin.ModelAdmin):
    list_display = ('id_portfela', 'id_uslugi')
    fields = ('id_portfela', 'id_uslugi')


admin.site.register(Portfel, PortfelAdmin)
admin.site.register(Elementy_portfela)


# Register your models here.
