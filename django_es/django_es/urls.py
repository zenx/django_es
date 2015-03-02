from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

from django_es.apps.common.views import ExtraContextTemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_es.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', ExtraContextTemplateView.as_view(template_name='inicio.html',
                                                extra_context={'seccion':'home'}),
                                                name='inicio'),
    url(r'^que-es-django/$', ExtraContextTemplateView.as_view(template_name='intro.html',
                                                              extra_context={'seccion':'intro'}),
                                                              name='intro'),
    url(r'^descarga/$', ExtraContextTemplateView.as_view(template_name='descarga.html',
                                                         extra_context={'seccion':'descarga'}),
                                                         name='descarga'),
    url(r'^blog/', include('apps.blog.urls')),
    url(r'^blog/', include('apps.docs.urls')),
    url(r'^blog/', include('apps.empleo.urls')),
    url(r'^comunidad/', include('apps.feeds.urls')),
    url(r'^formacion/', include('apps.formacion.urls')),
    url(r'^libros/', include('apps.libros.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
