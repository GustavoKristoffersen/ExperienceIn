from django.urls import path
from usuarios import views

urlpatterns = [
    path('registrar', views.RegistrarUsuarioView.as_view(), name="registrar"),
]