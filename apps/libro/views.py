from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class InicioView(TemplateView):
    template_name = "index.html"

class AutorListView(ListView):
    model = Autor
    template_name = "libro/listar_autor.html"
    context_object_name='autores'
    queryset = Autor.objects.filter(estado=True)


class AutorUpdateView(UpdateView):
    model = Autor
    template_name = "libro/crear_autor.html"
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')


class AutorCreateView(CreateView):
    model = Autor
    template_name = 'libro/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'libro/eliminar_autor.html'

    def post(self, request, pk, *args, **kwargs):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')


def eliminarAutor(request, id):
    autor = Autor.objects.get(id=id)

    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')

    return render(request, 'libro/eliminar_autor.html', {'autor': autor})
