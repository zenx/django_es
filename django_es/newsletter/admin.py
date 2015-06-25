# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Suscriptor


@admin.register(Suscriptor)
class SuscriptorAdmin(admin.ModelAdmin):
    list_display = ['email', 'creado', 'activo']
    list_editable = ['activo']
    list_filter = ['activo', 'creado']
