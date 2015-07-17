# -*- encoding: utf-8 -*-
from django.conf import settings
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.html import linebreaks, urlize, escape

from django.db.models import Count
from django.core.exceptions import FieldError

from .models import Entrada

from taggit.models import TaggedItem, Tag

import datetime

def year_archive(request, anio):
    section = 'blog'
    months = Entrada.objects.filter(estado='publicado', publicado__year=year).dates('publicado', 'month', order='DESC')

    if request.path.startswith('/es/web/'):
        return render_to_response('web/blog/archives/year.html', locals(), context_instance=RequestContext(request))
    return render_to_response('blog/archives/year.html', locals(), context_instance=RequestContext(request))


def month_archive(request, anio, mes):
    section = 'blog'
    month_date = datetime.date(int(year), int(month), 1)
    posts = Entrada.objects.filter(estado='publicado', publicado__year=anio, publicado__month=mes)

    if request.path.startswith('/es/web/'):
        return render_to_response('web/blog/archives/month.html', locals(), context_instance=RequestContext(request))
    return render_to_response('blog/archives/month.html', locals(), context_instance=RequestContext(request))


def entrada_list(request, tag=None):
    objects = Entrada.objects.filter(estado='publicado')

    if tag:
        tag = get_object_or_404(Tag, slug=tag)
        objects = objects.filter(estado='publicado', tags__in=[tag])

    paginator = Paginator(objects, 6)
    page = int(request.GET.get('page', '1'))

    page = request.GET.get('page')
    try:
        entradas = paginator.page(page)
    except PageNotAnInteger:
        entradas = paginator.page(1)
    except EmptyPage:
        entradas = paginator.page(paginator.num_pages)

    return render(request, 'blog/entrada/list.html', {'seccion':'blog',
                                                      'entradas': entradas,
                                                      'tag': tag})


def entrada_detail(request,entrada):
    entrada = get_object_or_404(Entrada, slug=entrada,
                                         estado='publicado')

    entrada_tags_ids = entrada.tags.values_list('id', flat=True)
    entradas_similares = Entrada.objects.filter(estado='publicado',
                                                tags__in=entrada_tags_ids).exclude(id=entrada.id).annotate(mismos_tags=Count('tags')).order_by('-mismos_tags', '-publicado').distinct()

    return render(request, 'blog/entrada/detail.html', {'seccion': 'blog',
                                                        'entrada': entrada,
                                                        'entradas_similares': entradas_similares})


def autor_detail(request, username):
    user = get_object_or_404(User, username=username)
    entradas = user.entradas.filter(estado='publicado')
    return render(request, 'blog/autor/detail.html', {'seccion': 'blog',
                                                      'autor': entrada})


def blog_tag_list(request):
    request.LANGUAGE_CODE = 'es'
    section = 'blog'

    posts_ids = Post.objects.filter(language=request.LANGUAGE_CODE).values_list('id', flat=True)
    items_ids = TaggedItem.objects.filter(content_type__app_label='blog',
                                          object_id__in=posts_ids).values_list('tag_id', flat=True)
    tag_items_ids = TaggedItem.objects.filter(content_type__app_label='blog',
                                              object_id__in=posts_ids).values_list('id', flat=True)
    tags = Tag.objects.filter(id__in=items_ids)

    column_tags_number = len(tags) / 4
    try:
        tags = tags.filter(taggeditem_items__in=tag_items_ids).annotate(num_times=Count('taggeditem_items'))
    except FieldError:
        tags = tags.filter(taggit_taggeditem_items__in=tag_items_ids).annotate(num_times=Count('taggit_taggeditem_items'))

    tags = tags.order_by('-num_times')

    if request.path.startswith('/es/web/'):
        return render_to_response('web/blog/tag_list.html', locals(), context_instance=RequestContext(request))
    return render_to_response('blog/tag_list.html', locals(), context_instance=RequestContext(request))
