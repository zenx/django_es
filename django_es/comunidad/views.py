# -*- encoding: utf-8 -*-
import datetime
import feedparser
import urllib2

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Feed, FeedItem


def feed_comunidad(request):
    items = FeedItem.objects.all()[:30]
    return render(request, 'comunidad/feed/list.rss', {'items': items}, content_type='application/xml')


def listar_blogs(request):
    feeds = Feed.objects.filter(muerto=False)
    return render_to_response('comunidad/feed/blogs.html', {'seccion':'comunidad',
                                                            'blogs':feeds})


def listar_feeds(request):
    objects = FeedItem.objects.all()
    
    paginator = Paginator(objects, 6)
    page = int(request.GET.get('page', '1'))

    page = request.GET.get('page')
    try:
        feeds = paginator.page(page)
    except PageNotAnInteger:
        feeds = paginator.page(1)
    except EmptyPage:
        feeds = paginator.page(paginator.num_pages)
    
    return render(request, 'comunidad/feed/list.html', {'seccion':'comunidad',
                                                        'page': items})
    
