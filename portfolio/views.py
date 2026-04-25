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

from django.shortcuts import get_object_or_404, render
from .models import Docente

def detalhe_docente(request, id):
    docente = Docente.objects.get(id=id)

    return render(request, "portfolio/detalhe_docente.html", { "docente": docente })

def projetos_view(request):
    projetos = Projeto.objects.all()

    return render(request, "portfolio/projetos.html", {"projetos": projetos})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()

    return render(request, "portfolio/tecnologias.html", {"tecnologias": tecnologias })

def competencias_view(request):
    competencias = Competencia.objects.all()

    return render(request, "portfolio/competencias.html", {"competencias": competencias})

def makingof_view(request):
    makingof = MakingOf.objects.all()
    
    return render(request, "portfolio/makingof.html", {'makingof':makingof})