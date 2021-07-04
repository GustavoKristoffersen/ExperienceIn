from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfis/<int:id>', views.exibir, name='exibir'),
    path('perfis/<int:id>/convidar', views.convidar, name='convidar'),
    path('convite/<int:convite_id>/aceitar', views.aceitar, name='aceitar'),
]