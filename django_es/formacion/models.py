# -*- encoding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from common.models import Pais

TIPO_CHOICES = (
    ('charla', 'Charla'),
    ('conferencia', 'Conferencia'),
    ('curso', 'Curso'),
    ('taller', 'Taller'),
    ('evento', 'Evento'),
)


class Organizador(models.Model):
    nombre = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.nombre


class Curso(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    organizadores = models.ManyToManyField(Organizador, related_name='cursos', blank=True)
    lugar = models.CharField(max_length=250)
    precio = models.CharField(max_length=250)
    pais = models.ForeignKey(Pais, related_name='cursos')
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(blank=True, max_length=250)
    descripcion = models.TextField(blank=True)
    fecha_inscripcion = models.DateField(blank=True, null=True)
    fecha_ini = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    web = models.URLField(blank=True)
    activo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    pago_online = models.BooleanField(default=False)

    class Meta:
        ordering = ('-fecha_ini',)
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('formacion:curso_detail', args=[self.slug])


class Alta(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    nif = models.CharField(max_length=11)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    pagado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-creado',)
        
    def __str__(self):
        return self.nombre
