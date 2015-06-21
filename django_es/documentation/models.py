# -*- encoding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# django imports
from django.db import models


class Node(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    document = models.CharField(max_length=256)
    source = models.TextField()

