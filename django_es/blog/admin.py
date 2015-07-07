# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Entrada, PerfilAutor
from .forms import EntradaAdminForm


def previsualizar(obj):
    return '<a href="{}" target="_blank">Ver</a>'.format(obj.get_absolute_url())
previsualizar.allow_tags = True


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            return EntradaAdminForm
        return super(EntradaAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            # un usuario sólo puede gestionar sus posts
            obj.user = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(EntradaAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            # un usuario sólo puede ver sus posts
            return qs.filter(user=request.user)
        return qs


@admin.register(PerfilAutor)
class PerfilAutorAdmin(admin.ModelAdmin):
    list_display = ['autor', 'web']
