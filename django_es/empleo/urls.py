# -*- encoding: utf-8 -*-

# django imports
from django.conf.urls import url

# django-es imports
import views


urlpatterns = [
    url(r'^$', views.oferta_list, name='oferta_list'),
    url(r'^pais/(?P<pais>[-\w]{2})/$', views.oferta_list, name='oferta_list_por_pais'),
    url(r'^(?P<oferta>[-\w]+)/$', views.oferta_detail, name='oferta_detail'),
    url(r'^oferta/publicar/$', views.oferta_publicar, name='oferta_publicar'),
    #url(r'^(?P<oferta>[-\w]+)/aplicar/$', views.oferta_detail, name='oferta_detail'),
]
