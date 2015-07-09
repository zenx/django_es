# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from common.models import Pais
from .models import Curso
from .forms import AltaForm


def curso_list(request, pais=None):
    paises = Pais.objects.filter(es_hispano=True)
    cursos = Curso.objects.filter(activo=True)
    if pais:
        pais = get_object_or_404(Pais, codigo=pais, es_hispano=True)
        cursos = cursos.filter(pais=pais)
    return render(request, 'formacion/curso/list.html', {'seccion': 'formacion',
                                                         'cursos': cursos})


def curso_detail(request, oferta):
    curso = get_object_or_404(Curso, slug=slug)
    formulario_alta = None
    if timezone.now() < curso.fecha_inscripcion:
        formulario_alta = AltaForm()
    return render(request, 'formacion/curso/detail.html', {'seccion': 'formacion',
                                                           'curso': curso})
