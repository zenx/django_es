# -*- encoding: utf-8 -*-
from django import template
from ..models import FeedItem


register = template.Library()


@register.assignment_tag
def get_feed_items(number):
    return FeedItem.objects.all()[:number]
