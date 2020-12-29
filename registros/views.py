from django.shortcuts import render, redirect
from .models import categorias
from .form import categoriasform
import datetime
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
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

class categoriasCreateView(CreateView):
    model = categorias
    fields = '__all__'
    success_url = reverse_lazy("url_listagem")

def delete(request, pk):
    Categorias = categorias.objects.filter(pk=pk)
    Categorias.delete()
    return redirect('url_listagem')

class categoriasUpdateView(UpdateView):
    model = categorias
    fields = '__all__'
    success_url = reverse_lazy("url_listagem")

