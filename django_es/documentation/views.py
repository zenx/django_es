# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# python imports
import os

# django imports
from django.conf import settings
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

# 3rd. party imports
from sphinx.websupport import WebSupport
from sphinx.websupport.errors import DocumentNotFoundError

# app imports
from .storages import ORMStorage


def get_document(request, docname=None):
    if not docname:
        docname = 'index'
    datadir = os.path.join(settings.BASE_DIR, 'documentation/output/data')
    support = WebSupport(datadir=datadir,
                         search='xapian',
                         storage=ORMStorage())

    try:
        document = support.get_document(docname)
    except DocumentNotFoundError:
        raise Http404('Document not found.')
    return render_to_response('doc.html',
                              {'seccion': 'docs',
                               'request': request,
                               'document': document},
                              context_instance=RequestContext(request))
