from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, id):
    perfil = Perfil()
    
    if id == 1:
        perfil = Perfil('Gustavo William', 'gustavo.oliveira1@estudante.ifb.edu.br', '222222', 'IFB')
    if id == 2:
        perfil = Perfil('Elon Musk', 'elon.musk@tesla.com', '333333', 'Tesla') 

    return render(request, 'perfil.html', {'perfil': perfil})

