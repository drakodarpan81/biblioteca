from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView
# Create your views here.

class InicioView(TemplateView):
    template_name = "index.html"

class AutorListView(ListView):
    model = Autor
    template_name = "libro/listar_autor.html"
    context_object_name='autores'
    queryset = Autor.objects.filter(estado=True)


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
