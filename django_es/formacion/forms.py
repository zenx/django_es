# -*- encoding: utf-8 -*-
from django import forms
from .models import Alta


class AltaForm(forms.ModelForm):
    class Meta:
        model = Alta
        fields = ['nombre', 'apellidos', 'nif']