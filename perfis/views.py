from django.shortcuts import render
from perfis.models import Perfil
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, id):
    perfil = Perfil.objects.get(id=id)

    return render(request, 'perfil.html', {'perfil': perfil})

