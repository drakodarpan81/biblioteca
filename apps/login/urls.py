from django.urls import path
from .views import *

urlpatterns = [
    # path('inicio_usuarios/', InicioListadoView.as_view(), name = 'inicio_usuarios'),
    path('listado_usuarios/', UsuarioListView.as_view(), name = 'listar_usuarios'),
    path('registrar_usuarios/', RegistrarUsuario.as_view(), name = 'registrar_usuarios' ),
]
