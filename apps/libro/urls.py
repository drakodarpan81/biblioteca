from django.urls import path
from .views import *

urlpatterns = [
    # Autores
    path('listar_autor/', AutorListView.as_view(), name='listar_autor'),
    path('editar_autor/<int:pk>', AutorUpdateView.as_view(), name='editar_autor'),
    path('crear_autor/', AutorCreateView.as_view(), name='crear_autor'),
    path('eliminar_autor/<int:pk>',
         AutorDeleteView.as_view(), name='eliminar_autor'),

    # Libros
    path('listar_libros/', LibroListView.as_view(), name='listado_libros'),
    path('crear_libro/', LibroCreateView.as_view(), name='crear_libro'),
    path('editar_libro/<int:pk>', LibroUpdateView.as_view(), name='editar_libro'),
    path('eliminar_libro/<int:pk>',
         LibroDeleteView.as_view(), name='eliminar_libro'),
]
