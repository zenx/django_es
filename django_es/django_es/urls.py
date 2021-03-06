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
    #url(r'^blog/', include('blog.urls')),
    #url(r'^docs/', include('docs.urls')),
    #url(r'^empleo/', include('empleo.urls')),
    #url(r'^comunidad/', include('feeds.urls')),
    #url(r'^formacion/', include('formacion.urls')),
    url(r'^libros/', include('libros.urls', namespace='libros')),
    
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
