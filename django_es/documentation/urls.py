# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# django imports
from django.conf.urls import patterns, url

# app imports
from .views import get_document


urlpatterns = patterns(
    '',
    url(r'^$', get_document, name='document_index'),
    url(r'^(?P<docname>[\w\-/]*?\w)/?$', get_document, name='document'),
)
