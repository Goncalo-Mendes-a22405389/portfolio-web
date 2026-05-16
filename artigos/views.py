from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def is_autor(user):
    return user.groups.filter(name='Autores').exists()

def lista_artigos(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')

    return render(request, 'artigos/artigos.html', { 'artigos': artigos, 'autor': is_autor(request.user)})

@login_required
def criar_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)

        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()

            return redirect('artigos')

    else:
        form = ArtigoForm()

    return render(request, 'artigos/novo_artigo.html', {
        'form': form
    })

@login_required    
def edita_artigo_view(request, artigo_id):

    artigo = Artigo.objects.get(id=artigo_id)
    
    if request.user != artigo.autor:
        return redirect('artigos')
    
    
    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos')
    else:
        form = ArtigoForm(instance=artigo)  
        
    context = {'form': form, 'artigo':artigo}
    return render(request, 'artigos/edita_artigo.html', context)

@login_required
def apaga_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    
    if request.user != artigo.autor:
        return redirect('artigos')
    
    artigo.delete()
    return redirect('artigos')

@login_required
def like_artigo(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    
    if request.user.is_authenticated:
        if request.user in artigo.likes.all():
            artigo.likes.remove(request.user)
        else:
            artigo.likes.add(request.user)
    return redirect("artigos")


def detalhe_artigo(request, artigo_id):

    artigo = Artigo.objects.get(id=artigo_id)

    comentarios = artigo.comentarios.all().order_by('-data_criacao')

    form = ComentarioForm()

    if request.method == 'POST':

        if not request.user.is_authenticated:
            return redirect('login')

        form = ComentarioForm(request.POST)

        if form.is_valid():

            comentario = form.save(commit=False)

            comentario.autor = request.user
            comentario.artigo = artigo

            comentario.save()

            return redirect('detalhe_artigo', artigo_id=artigo.id)

    context = {'artigo': artigo,'comentarios': comentarios,'form': form }

    return render(request, 'artigos/detalhe_artigo.html', context)