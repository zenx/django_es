# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# django imports
from django.core.management.base import BaseCommand

# app imports
from ...models import SphinxDocument


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        SphinxDocument.objects.build()
        self.stdout.write('Complete!')

