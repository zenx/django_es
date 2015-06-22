# -*- encoding: utf-8 -*-
import re
import urllib2

from django import template
from django.core.cache import cache


register = template.Library()

# Datos para parsear djangoproject.com
DJANGO_VERSION_REGEX = r'/download/([\d.]+)/tarball/'
DJANGO_DOWNLOAD_URL = 'https://www.djangoproject.com/download/'


@register.assignment_tag
def ultima_version_django():
    """
    Recuperar la ultima versión disponible de Django desde djangoproject.com.
    """
    # recuperar versión de Django de la cache
    ultima_version = cache.get('django_version', None)
    if not ultima_version:
        # si no está en cache recuperar última versión desde djangoproject.com
        ultima_version = None
        response = urllib2.urlopen(DJANGO_DOWNLOAD_URL)
        html = response.read()
        ultima_version_match = re.search(DJANGO_VERSION_REGEX, html)
        if ultima_version_match:
            ultima_version = ultima_version_match.group(1)
            cache.set('django_version', ultima_version)
    return ultima_version
