from django.db import models
from django.contrib.auth.models import User


class Feed(models.Model):
    titulo = models.CharField(max_length=250)
    feed_url = models.URLField(unique=True, max_length=250)
    public_url = models.URLField(max_length=250)
    muerto = models.BooleanField(default=False)

    class Meta:
        ordering = ("titulo",)

    def __str__(self):
        return self.titulo


class FeedItem(models.Model):
    feed = models.ForeignKey(Feed,related_name='items')
    titulo = models.CharField(max_length=250)
    link = models.URLField(max_length=250,unique=True,db_index=True)
    resumen = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    publicado = models.DateTimeField()

    class Meta:
        ordering = ("-publicado",)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return self.link
