from django.contrib import admin

from .models import Pais

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'es_hispano']
