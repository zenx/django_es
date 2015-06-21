from django import forms
from .models import Entrada


class EntradaAdminForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('titulo', 'slug', 'image', 'descripcion', 'rest', 'estado', 'tags')