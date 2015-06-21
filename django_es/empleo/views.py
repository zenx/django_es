# -*- encoding: utf-8 -*-
from django.shortcuts import render, render
from .models import Oferta


def oferta_list(request):
    ofertas = Oferta.objects.filter(activo=True)
    return render(request, 'empleo/oferta/list.html', {'seccion': 'empleo',
                                                       'ofertas': ofertas})

def oferta_detail(request, oferta):
    oferta = get_object_or_404(Oferta, slug=slug)
    return render(request, 'empleo/oferta/list.html', {'seccion': 'empleo',
                                                       'oferta': oferta})
