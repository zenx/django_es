# -*- encoding: utf-8 -*-
from django.db import models


class Suscriptor(models.Model):
    email = models.EmailField(db_index=True)
    creado = models.DateTimeField(db_index=True, auto_now_add=True)
    activo = models.BooleanField(db_index=True, default=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = u'suscriptor'
        verbose_name_plural = u'suscriptores'

    def __unicode__(self):
        return self.email
