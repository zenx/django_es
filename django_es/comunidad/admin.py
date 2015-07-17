from django.contrib import admin
from models import Feed, FeedItem


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'public_url', 'feed_url', 'muerto']
    list_filter = ['muerto']
    ordering = ['titulo']
    search_fields = ['titulo', 'public_url']


@admin.register(FeedItem)
class FeedItemAdmin(admin.ModelAdmin):
    list_display   = ['titulo', 'feed', 'creado', 'publicado', 'link']
    list_filter    = ['feed']
    search_fields  = ['feed__title', 'feed__public_url', 'title']
    date_heirarchy = ['publicado']
