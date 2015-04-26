# django imports
from django.conf.urls import patterns, include, url

# django-es imports
from .views import libro_list, libro_detail


urlpatterns = patterns('',
    url(r'^$', libro_list, name='libro_list'),
    url(r'^(?P<editorial_slug>[-\w]+)/$', libro_list, name='libro_list_by_editorial'),
    url(r'^(?P<editorial_slug>[-\w]+)/(?P<slug>[-\w]+)/$', libro_detail, name='libro_detail'),
)
