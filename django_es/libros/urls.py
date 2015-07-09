# django imports
from django.conf.urls import url

# django-es imports
from .views import libro_list, libro_detail


urlpatterns = [
    url(r'^$', libro_list, name='libro_list'),
    url(r'^editorial/(?P<editorial_slug>[-\w]+)/$', libro_list, name='libro_list_by_editorial'),
    url(r'^(?P<slug>[-\w]+)/$', libro_detail, name='libro_detail'),
]
