from django.shortcuts import render
from .models import *
# Create your views here.


def index_view(request):
    return render(request, 'portfolio/base.html')


def tfc_view(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/tfc.html', {'tfcs' : tfcs})

def licenciatura_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request,'portfolio/licenciatura.html', {'licenciaturas' : licenciaturas})


def detalhe_licenciatura(request, id):
    licenciatura = Licenciatura.objects.get(id=id)
    anos = licenciatura.anos.all()

    return render(request, "portfolio/detalhe_licenciatura.html", {"licenciatura": licenciatura,"anos": anos})

def detalhe_ano(request, id):
    ano = Ano.objects.get(id=id)
    ucs = ano.ucs.all()

    return render(request, "portfolio/detalhe_ano.html", {"ano": ano,"ucs": ucs})