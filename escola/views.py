from django.shortcuts import render
from .models import *
# Create your views here.

def cursos_view(request):

    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    
    return render(request, 'escola/cursos.html', {'cursos': cursos})

def curso_view(request, id):

    curso=Curso.objects.get(id=id)    
       
    return render(request, 'escola/curso.html', {'curso': curso})


def aluno_view(request):

    alunos = Aluno.objects.all()
    
    return render(request, 'escola/alunos.html', {'alunos': alunos})


def professor_view(request):

    professores = Professor.objects.all()
    
    return render(request, 'escola/professores.html', {'professores': professores})