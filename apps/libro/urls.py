from django.urls import path
from .views import *

urlpatterns = [
    path('listar_autor/', AutorListView.as_view(), name='listar_autor'),
    path('editar_autor/<int:pk>', AutorUpdateView.as_view(), name='editar_autor'),
    path('crear_autor/', AutorCreateView.as_view(), name='crear_autor'),
    path('eliminar_autor/<int:pk>', AutorDeleteView.as_view(), name='eliminar_autor'),
]
