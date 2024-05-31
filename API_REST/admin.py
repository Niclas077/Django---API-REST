from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Vehiculos)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca','anyo','color')
    list_display_links =('marca',)


def datos(self,obj):
    return obj.marca.upper()