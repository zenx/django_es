# python imports
import datetime

# django imports
from django import template
from django.db.models import Count
from django.core.exceptions import FieldError

# lenergy imports
from ..models import Entrada

# 3rd. party libraries
from taggit.models import TaggedItem, Tag


register = template.Library()


@register.assignment_tag
def get_ultimas_entradas(number):
    return Entrada.objects.filter(estado='publicado').order_by('-publicado')[:number]
