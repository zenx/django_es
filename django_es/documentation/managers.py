# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# python imports
import logging
import os

# django imports
from django.db import models
from django.conf import settings

# app imports
from .storages import ORMStorage
from .websupport import WebSupport

logger = logging.getLogger(__name__)


class DocumentManager(models.Manager):
    """
    """
    def __init__(self, storage=None):
        if storage is None:
            srcdir = os.path.join(settings.BASE_DIR,
                                  'documentation/src')
            builddir = os.path.join(settings.BASE_DIR,
                                    'documentation/output')
            datadir = os.path.join(settings.BASE_DIR,
                                   'documentation/output/data')
            self._support = WebSupport(srcdir=srcdir,
                                       builddir=builddir,
                                       datadir=datadir,
                                       search='xapian',
                                       docroot='docs',
                                       storage=ORMStorage(self))
        super(DocumentManager, self).__init__()

    def build(self):
        self._support.build()

    def get_document(self, docname, username='', moderator=False):
        return self._support.get_document(docname, username, moderator)

    def get_search_results(self, q):
        return self._support.get_search_results(q)

