from django.shortcuts import render, redirect
from .models import categorias
from .form import categoriasform
import datetime

# Create your views here.

def home(request):
    data = {}
    data['desejos'] = ['Aprendizado','Desenvolvimento pessoal','Experiência']
    data['agora'] = datetime.datetime.now()

    return render(request, 'registros/home.html', data)

def listagem(request):
    data = {}
    data['categorias'] = categorias.objects.all()
    return render(request, 'registros/listagem.html', data)

def novo_dado(request):
    data = {}
    form = categoriasform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    return render(request, 'registros/form.html', data)

def update(request, pk):
    data = {}
    Categorias = categorias.objects.filter(pk=pk)
    form = categoriasform(request.POST or None, instance=Categorias)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['categorias'] = categorias
    return render(request, 'registros/form.html', data)

def delete(request, pk):
    Categorias = categorias.objects.filter(pk=pk)
    Categorias.delete()
    return redirect('url_listagem')