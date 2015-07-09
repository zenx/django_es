# -*- encoding: utf-8 -*-
from django import template
from ..models import Libro


register = template.Library()


@register.assignment_tag
def get_libros_recomendados(number):
    return Libro.objects.filter(recomendado=True)[:number]
