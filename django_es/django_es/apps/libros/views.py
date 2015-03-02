from django.shortcuts import render

def libro_detalle(request):
    
    return render(request, 'account/dashboard.html', locals())