from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView
# Create your views here.

"""
    dispatch => Valida la petición y elige que methodo HTTP se utilizo en la solicitud
    http_method_not_allowed => Error cuando se utiliza un método HTTP no soportado


class InicioView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
"""

class InicioView(TemplateView):
    template_name = "index.html"


def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            nom = autor_form.cleaned_data['nombre']
            print(nom)

            autor_form.save()
            return render(request, 'index.html')
    else:
        autor_form = AutorForm()

    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})


def listarAutor(request):
    autores = Autor.objects.filter(estado=True)

    return render(request, 'libro/listar_autor.html', {'autores': autores})


def editarAutor(request, id):

    autor_form = None
    error = None

    try:

        autor = Autor.objects.get(id=id)

        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('libro:listar_autor')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error': error})


def eliminarAutor(request, id):
    autor = Autor.objects.get(id=id)

    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')

    return render(request, 'libro/eliminar_autor.html', {'autor': autor})
