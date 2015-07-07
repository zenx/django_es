# -*- encoding: utf-8 -*-
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

from django_thumbs.fields import ImageWithThumbsField
from django.core.urlresolvers import reverse
from django.conf import settings        
from django.utils.translation import activate
from django.contrib.sitemaps import ping_google

from taggit.managers import TaggableManager


class PerfilAutor(models.Model):
    autor = models.OneToOneField(User,related_name='perfil_blog')
    imagen = ImageWithThumbsField(blank=True, upload_to='blog/autores/%Y/%m/%d', sizes=((160,160),))
    web = models.URLField(blank=True)
    descripcion = models.TextField()
    
    def __unicode__(self):
        return self.autor.get_full_name()


class EntradaManager(models.Manager):
    def publicadas(self):
        return self.filter(publico=True)


class Entrada(models.Model):
    ESTADO_CHOICES = (
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField('título', max_length=250)
    autor = models.ForeignKey(User,
                              related_name='entradas_blog', null=True)
    slug = models.SlugField(max_length=250,
                            unique=True,
                            blank=True,
                            help_text='Usado para las URLs. No cambiar una vez publicado.')
    image = ImageWithThumbsField(blank=True,
                                 upload_to='blog/articulos/%Y/%m/%d',
                                 sizes=((40,40),(100,100),(160,160),(290,0), (630,0)))
    descripcion = models.TextField('descripción', help_text='Texto plano para utilizar en el feed RSS')
    rest = models.TextField('markdown', help_text='Cuerpo del artículo. Se puede utilizar el formato Markdown y HTML.')
    html = models.TextField(blank=True, editable=False)
    estado = models.CharField(max_length='10', choices=ESTADO_CHOICES, default='borrador')
    tags = TaggableManager(blank=True)
    
    objects = EntradaManager()

    # fechas
    publicado = models.DateTimeField('fecha de publicación', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('-publicado',)
        
    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog:entrada_detail', args=[self.slug])

    def save(self, *args, **kwargs): 
        #from markdown import markdown
        #self.html = markdown(self.body)
        super(Entrada, self).save(*args, **kwargs)
        if self.estado == 'publicado':
            try:
                ping_google()
            except Exception:
                pass
"""

class Comentario(models.Model):
    entrada = models.ForeignKey(Entrada, related_name="comentarios")
    nombre = models.CharField(max_length=80)
    email = models.EmailField()
    url = models.URLField(blank=True)
    texto = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    bloqueado = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['id']
    
    def save(self, *args, **kwargs):
        send_mail('[Django-Blog] Nuevo comentario en "%s"' % self.entrada, '%s (%s) dice:\n\n %s' % (self.nombre, self.email, self.texto), 'antonio.mele@django.es', ['antonio.mele@django.es'], fail_silently=True)
        super(Comentario, self).save()
        
    def __str__(self):
        return self.texto
"""