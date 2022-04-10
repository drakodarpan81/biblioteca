from django.urls import path
from .views import *

urlpatterns = [
    path('crear_autor/', crearAutor, name='crear_autor'),
    path('editar_autor/<int:id>', editarAutor, name='editar_autor'),
    path('eliminar_autor/<int:id>', eliminarAutor, name='eliminar_autor'),
    path('', InicioView.as_view(), name='index'),
    path('listar_autor/', AutorListView.as_view(), name='listar_autor'),
]
