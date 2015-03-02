from django.shortcuts import render
from django.views.generic.base import TemplateView
from .utils import obtener_ultima_version_django


class ExtraContextTemplateView(TemplateView):
    extra_context = {}
    def get_context_data(self, **kwargs):
        context = super(ExtraContextTemplateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

def inicio(request):
    ultima_version = obtener_ultima_version_django()