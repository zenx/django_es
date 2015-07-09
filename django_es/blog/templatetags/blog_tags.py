# -*- encoding: utf-8 -*-
from django import template
from ..models import Entrada


register = template.Library()


@register.assignment_tag
def get_ultimas_entradas(number):
    return Entrada.objects.filter(estado='publicado').order_by('-publicado')[:number]
