# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# django imports
from django.conf.urls import patterns, url

# app imports
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.get_document, name='index'),
    url(r'^search/?$', views.search_documents, name='search'),
    url(r'^(?P<docname>[\w\-/]*?\w)/?$', views.get_document, name='document'),
)
