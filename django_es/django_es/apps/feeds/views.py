# -*- encoding: utf-8 -*-
import datetime
import feedparser
import urllib2

from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from .models import Feed, FeedItem
from utils.digg_paginator import DiggPaginator


def feed_comunidad(request):
    items = FeedItem.objects.all()[:30]
    return render_to_response('comunidad/feed.rss', { 'items': items, }, mimetype='application/xml', context_instance=RequestContext(request))

def listar_blogs(request):
    feeds = Feed.objects.filter(muerto=False)
    return render_to_response('comunidad/listar_blogs.html',{'blogs':feeds, 'seccion':'comunidad' }, context_instance=RequestContext(request))

def listar_feeds(request):
    objects = FeedItem.objects.all()
    paginator = DiggPaginator(objects, 10, body=5, padding=2, tail=3)
    
    page = int(request.GET.get('page', '1'))
    
    #grab the current page from the paginator...
    items = paginator.page(page)
    return render_to_response('comunidad/listar_feeds.html', { 'page': items, 'seccion':'comunidad' }, context_instance=RequestContext(request))
    
def actualizar_feeds(request):
    # detectar feeds muertos (aka error 404)
    for f in Feed.objects.filter(muerto=False):
        try:
            r = urllib2.urlopen(f.feed_url)
        except urllib2.HTTPError, e:
            if e.code == 404 or e.code == 500:
                f.muerto = True
                f.save()
            else:
                raise
    # obtener feeds
    for f in Feed.objects.filter(muerto=False):
        
        feed = feedparser.parse(f.feed_url)
        for i in range(len(feed.entries)):
            
            e = feed['entries'][i]
            
            pub_date = e.updated_parsed
            publicado = datetime.date(pub_date[0], pub_date[1], pub_date[2] )
            
            titulo = e.title
            
            if hasattr(e, 'summary'):
                resumen = e.summary
            else:
                resumen = e.content[0]['value']
            link = e.link
            
            try:
                FeedItem.objects.get(link=link)
            except ObjectDoesNotExist:
                FeedItem.objects.create(feed=f,titulo=titulo,link=link,resumen=resumen,publicado=publicado)
    
    return HttpResponse('actualizado :)')