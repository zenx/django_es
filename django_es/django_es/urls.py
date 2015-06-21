# -*- encoding: utf-8 -*-

# django imports
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

# django-es imports
from common.views import ExtraContextTemplateView


urlpatterns = patterns('',
    url(r'^$', ExtraContextTemplateView.as_view(template_name='inicio.html',
                                                extra_context={'seccion':'home'}),
                                                name='inicio'),
    url(r'^que-es-django/$', ExtraContextTemplateView.as_view(template_name='intro.html',
                                                              extra_context={'seccion':'intro'}),
                                                              name='intro'),
    url(r'^descarga/$', ExtraContextTemplateView.as_view(template_name='descarga.html',
                                                         extra_context={'seccion':'descarga'}),
                                                         name='descarga'),

    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^docs/', include('documentation.urls', namespace='docs')),
    url(r'^empleo/', include('empleo.urls', namespace='empleo')),
    url(r'^comunidad/', include('comunidad.urls', namespace='comunidad')),
    url(r'^formacion/', include('formacion.urls', namespace='formacion')),
    url(r'^libros/', include('libros.urls', namespace='libros')),
    
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
