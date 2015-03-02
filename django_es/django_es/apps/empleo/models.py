# -*- encoding: utf-8 -*-
from django.db import models


PAISES = (
    ('España','es'),
    ('Alemania','de'),
    ('Brasil','br'),
    ('Francia','fr'),
)

class Oferta(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    remuneracion = models.CharField(max_length=250, blank=True)
    pais = models.CharField(choices=PAISES, max_length=2)
    ciudad = models.CharField(max_length=250, blank=True)
    empresa = models.CharField(max_length=80)
    email = models.EmailField()
    url = models.URLField(blank=True)
    contacto = models.CharField(max_length=250, blank=True)
    
    def __unicode__(self):
        return self.titulo
        
    