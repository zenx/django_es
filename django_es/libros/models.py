# -*- encoding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse


class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,
                            unique=True)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField('título', max_length=250, db_index=True)
    slug = models.SlugField(max_length=100,
                            unique=True)
    autor = models.CharField('autor', max_length=120)
    editorial = models.ForeignKey(Editorial, related_name='libros')
    anio = models.PositiveIntegerField('año')
    portada = models.ImageField(upload_to='libros/')
    url = models.URLField()
    descripcion = models.TextField(blank=True)
    recomendado = models.BooleanField(default=False)

    class Meta:
        ordering = ('-anio', 'id')

    def get_absolute_url(self):
        return reverse('libros:libro_detail', args=[self.slug])

    def __str__(self):
        return self.titulo
