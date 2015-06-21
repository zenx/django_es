# -*- encoding: utf-8 -*-
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import entrada_list, entrada_detail
from .feeds import UltimasEntradasFeed

urlpatterns = [
    url(r'^$', entrada_list, name='entrada_list'),
    url(r'^(?P<entrada>[-\w]+)/$', entrada_detail, name='entrada_detail'),
    #url(r'^(?P<anio>\d{4})/(?P<mes>\d{2})/$', month_archive, name='blog_month_archive'),
    #url(r'^(?P<anio>\d{4})/$', year_archive, name='blog_year_archive'),
    #url(r'^tag/(?P<slug>[-\w]+)/$', blog_tag_post_list, name='blog_tag_post_list'),
    #url(r'^tags/', blog_tag_list, name='blog_tag_list'),
    url(r'^feed/$', UltimasEntradasFeed(), name='blog_latest_posts_feed'),
]