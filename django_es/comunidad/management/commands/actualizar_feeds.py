# -*- encoding: utf-8 -*-
import datetime
import feedparser
import urllib2
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from ...models import Feed, FeedItem


class Command(BaseCommand):

    def handle(self, *args, **options):
        # detectar feeds muertos (error 404 o 500)
        for f in Feed.objects.filter(muerto=False):
            try:
                r = urllib2.urlopen(f.feed_url)
            except urllib2.HTTPError, e:
                if e.code in [404, 500]:
                    f.muerto = True
                    f.save()

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
                    FeedItem.objects.create(feed=f,
                                            titulo=titulo,
                                            link=link,
                                            resumen=resumen,
                                            publicado=publicado)
