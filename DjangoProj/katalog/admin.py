from django.contrib import admin
from katalog.models import Usluga, Oprocentowanie, Wartosc

class UslugaAdmin(admin.ModelAdmin):
    list_display = ('typ_uslugi', 'id_uslugi')

class OprocentownieAdmin(admin.ModelAdmin):
    list_display = ('oprocentowanie',)

class WartoscAdmin(admin.ModelAdmin):
    list_display = ('wartosc_0', 'wartosc_t')

admin.site.register(Usluga, UslugaAdmin)
admin.site.register(Oprocentowanie, OprocentownieAdmin)
admin.site.register(Wartosc, WartoscAdmin)
# Register your models here.
