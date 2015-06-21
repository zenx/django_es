# django imports
from django.conf.urls import url

# django-es imports
from .views import curso_list, curso_detail


urlpatterns = [
    url(r'^$', curso_list, name='curso_list'),
    url(r'^(?P<pais>[-\w]{2})/$', curso_detail, name='curso_list_por_pais'),
    url(r'^curso/(?P<curso>[-\w]+)/$', curso_detail, name='curso_detail'),
]