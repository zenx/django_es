import re
import urllib2
from django import template
from django.core.cache import cache


register = template.Library()


DJANGO_VERSION_REGEX = r'/download/([\d.]+)/tarball/'
DJANGO_DOWNLOAD_URL = 'https://www.djangoproject.com/download/'


@register.assignment_tag
def ultima_version_django():
    """
    Recuperar la ultima version disponible de Django desde djangoproject.com.
    """
    ultima_version = cache.get('django_version', None)
    if not ultima_version:
        ultima_version = None
        response = urllib2.urlopen(DJANGO_DOWNLOAD_URL)
        html = response.read()
        latest_version_match = re.search(DJANGO_VERSION_REGEX, html)
        if latest_version_match:
            ultima_version = latest_version_match.group(1)
            cache.set('django_version', ultima_version)
    return ultima_version
