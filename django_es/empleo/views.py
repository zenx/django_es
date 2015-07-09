# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from common.models import Pais
from .models import Oferta
from .forms import OfertaForm


def oferta_list(request, pais=None):
    ofertas = Oferta.objects.filter(activo=True)
    paises = Pais.objects.all()
    if pais:
        pais = get_object_or_404(Pais, codigo=pais, es_hispano=True)
        ofertas = ofertas.filter(pais=pais)

    return render(request, 'empleo/oferta/list.html', {'seccion': 'empleo',
                                                       'ofertas': ofertas,
                                                       'paises': paises,
                                                       'pais': pais})

def oferta_detail(request, oferta):
    oferta = get_object_or_404(Oferta, slug=oferta)
    return render(request, 'empleo/oferta/detail.html', {'seccion': 'empleo',
                                                         'oferta': oferta})


def oferta_publicar(request):
    form = OfertaForm()
    if request.method == 'POST':
        form = OfertaForm(data=request.DATA,
                          files=request.FILES)
    return render(request, 'empleo/oferta/publicar.html', {'seccion': 'empleo',
                                                           'oferta': oferta})
