# -*- encoding: utf-8 -*-

# django imports
from django.conf.urls import url

# django-es imports
from .views import oferta_list, oferta_detail


urlpatterns = [
    url(r'^$', oferta_list, name='oferta_list'),
    url(r'^(?P<oferta>[-\w]+)/$', oferta_detail, name='oferta_detail'),
]