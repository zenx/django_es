# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .models import Libro, Editorial


def libro_detail(request, slug):
    seccion = 'libros'
    libro = get_object_or_404(Libro, slug=slug)
    return render(request, 'libros/libro/detail.html', {'seccion': 'libros',
                                                        'libro': libro})


def libro_list(request, editorial_slug=None):
    seccion = 'libros'
    editoriales = Editorial.objects.annotate(total_libros=Count('libros'))
    objects = Libro.objects.all()
    if editorial_slug:
        editorial = get_object_or_404(Editorial, slug=editorial_slug)
        objects = objects.filter(editorial=editorial)

    paginator = Paginator(objects, 6)
    page = int(request.GET.get('page', '1'))

    page = request.GET.get('page')
    try:
        libros = paginator.page(page)
    except PageNotAnInteger:
        libros = paginator.page(1)
    except EmptyPage:
        libros = paginator.page(paginator.num_pages)

    return render(request, 'libros/libro/list.html', locals())
