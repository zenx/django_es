# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# python imports
import os

# django imports
from django.conf import settings
from django.core.management.base import BaseCommand

# 3rd. party imports
from sphinx.websupport import WebSupport

# app imports
from ...storages import ORMStorage


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        srcdir = os.path.join(settings.BASE_DIR, 'documentation/src')
        builddir = os.path.join(settings.BASE_DIR, 'documentation/output')
        support = WebSupport(srcdir=srcdir,
                             builddir=builddir,
                             search='xapian',
                             storage=ORMStorage())
        support.build()
        self.stdout.write('Complete!')

