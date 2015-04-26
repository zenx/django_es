# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=250, verbose_name=b't\xc3\xadtulo')),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('autor', models.CharField(max_length=120, verbose_name=b'autor')),
                ('anio', models.PositiveIntegerField(verbose_name=b'a\xc3\xb1o')),
                ('portada', models.ImageField(upload_to=b'libros/')),
                ('url', models.URLField()),
                ('descripcion', models.TextField(blank=True)),
                ('editorial', models.ForeignKey(related_name='libros', to='libros.Editorial')),
            ],
            options={
                'ordering': ('-anio', 'id'),
            },
        ),
    ]
