# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# django imports
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

# 3rd. party imports
from sphinx.websupport.errors import DocumentNotFoundError

# project imports
from common.forms import SearchForm

# app imports
from .models import SphinxDocument


def get_document(request, docname=None):
    if not docname:
        docname = 'index'
    try:
        document = SphinxDocument.objects.get_document(docname)
    except DocumentNotFoundError:
        raise Http404('Document not found.')
    return render_to_response('doc.html',
                              {'seccion': 'docs',
                               'request': request,
                               'document': document,
                               'form': SearchForm()},
                              context_instance=RequestContext(request))


def search_documents(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data.get('query')
    else:
        query = ''

    search_results = list(SphinxDocument.objects.get_search_results(query))
    paginator = Paginator(search_results, 10)
    page = request.GET.get('page', None)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        search_results = paginator.page(paginator.num_pages)

    return render_to_response('searchresults.html',
                              {'seccion': 'docs',
                               'request': request,
                               'search_results': search_results,
                               'form': SearchForm()},
                              context_instance=RequestContext(request))

