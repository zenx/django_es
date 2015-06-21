# -*- encoding: utf-8 -*-

from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from .models import Entrada


class UltimasEntradasFeed(Feed):
    title = 'Blog de Django-es'
    link = '/blog/'
    description = 'Últimas entradas de Django.es'

    title_template = 'blog/feeds/title.txt'
    description_template = 'blog/feeds/description.txt'
    
    def item_pubdate(self, item):
        return item.publicado
                
    def items(self):
        return Entrada.objects.filter(status='publicado').order_by('-publicado')[:10]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.html
