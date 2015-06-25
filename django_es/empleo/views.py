# -*- encoding: utf-8 -*-
from django.shortcuts import render, render
from common.models import Pais
from .models import Oferta


def oferta_list(request, pais=None):
    ofertas = Oferta.objects.filter(activo=True)
    paises = Pais.objects.all()
    if pais:
        pais = get_object_or_404(Pais, codigo=pais, es_hispano=True)
        ofertas = ofertas.filter(pais=pais)

    return render(request, 'empleo/oferta/list.html', {'seccion': 'empleo',
                                                       'ofertas': ofertas})

def oferta_detail(request, oferta):
    oferta = get_object_or_404(Oferta, slug=slug)
    return render(request, 'empleo/oferta/list.html', {'seccion': 'empleo',
                                                       'oferta': oferta})
