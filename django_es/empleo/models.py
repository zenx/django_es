# -*- encoding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from common.models import Pais


class Oferta(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    descripcion = models.TextField()
    remuneracion = models.CharField(max_length=250, blank=True)
    pais = models.ForeignKey(Pais,
                             related_name='ofertas')
    ciudad = models.CharField(max_length=250, blank=True)
    empresa = models.CharField(max_length=80)
    email = models.EmailField()
    url = models.URLField(blank=True)
    contacto = models.CharField(max_length=250, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('empleo:oferta_detail', args=[self.slug])
