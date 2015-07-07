# -*- encoding: utf-8 -*-
from django import forms
from .models import Suscriptor


class SuscriptorForm(forms.ModelForm):
    class Meta:
        model = Suscriptor
        fields = ['email']
