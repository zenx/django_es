# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# django imports
from django.db import models

# app imports
from .managers import DocumentManager


class SphinxDocument(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    document = models.CharField(max_length=256)
    source = models.TextField()

    objects = DocumentManager()

