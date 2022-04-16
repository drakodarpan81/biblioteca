from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AutorForm, LibroForm
from .models import *


class InicioView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


class AutorListView(LoginRequiredMixin, ListView):
    model = Autor
    template_name = "libro/autor/listar_autor.html"
    context_object_name = 'autores'
    form_class = AutorForm

    def get_queryset(self):
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = {}
        context["autores"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
        

class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    template_name = "libro/autor/crear_autor.html"
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')


class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    template_name = 'libro/autor/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')


class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    template_name = 'libro/autor/eliminar_autor.html'

    def post(self, request, pk, *args, **kwargs):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')


class LibroListView(LoginRequiredMixin, ListView):
    model = Libro
    template_name = "libro/libro/listar_libro.html"
    context_object_name = 'libros'
    queryset = Libro.objects.filter(estado=True)
    context_object_name = 'libros'


class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "libro/libro/crear_libro.html"
    success_url = reverse_lazy('libro:listado_libros')


class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    template_name = "libro/libro/crear_libro.html"
    success_url = reverse_lazy('libro:listado_libros')
    form_class = LibroForm


class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "libro/libro/eliminar_libro.html"
    success_url = reverse_lazy('libro:listado_libro')

    def post(self, request, pk, *args, **kwargs):
        object = Libro.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('libro:listado_libros')
