from django.contrib import admin
from globalnewartosci.models import TypUslugi, Stopa_rynkowa

class TypUslgiAdmin(admin.ModelAdmin):
    list_display = ('typ_uslugi',)

class Stopa_rynkowaAdmin(admin.ModelAdmin):
    list_display = ('st_rynkowa',)

admin.site.register(TypUslugi, TypUslgiAdmin)
admin.site.register(Stopa_rynkowa, Stopa_rynkowaAdmin)

# Register your models here.
