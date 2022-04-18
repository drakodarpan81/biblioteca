from django.urls import path
from .views import *

urlpatterns = [
    path('listado_usuarios/', UsuarioListView.as_view(), name = 'listar_usuarios' ),
    path('registrar_usuarios/', RegistrarUsuario.as_view(), name = 'registrar_usuarios' ),
]
