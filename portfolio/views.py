from django.shortcuts import render, redirect
from .models import *
from .forms import *
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

def novo_projeto_view(request):
    # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido. 
    # Senão, o form não tem dados e não é válido
    form = ProjetoForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('projetos')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_projeto.html', context)

def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    
    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)  # cria formulário com dados da instância autor
        
    context = {'form': form, 'projeto':projeto}
    return render(request, 'portfolio/edita_projeto.html', context)

def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('projetos')