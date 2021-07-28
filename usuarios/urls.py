from django.urls import path
from usuarios import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('registrar', views.RegistrarUsuarioView.as_view(), name="registrar"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
]