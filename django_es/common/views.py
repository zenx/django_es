# -*- encoding: utf-8 -*-
from django.views.generic.base import TemplateView


class ExtraContextTemplateView(TemplateView):
    extra_context = {}
    def get_context_data(self, **kwargs):
        context = super(ExtraContextTemplateView, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
