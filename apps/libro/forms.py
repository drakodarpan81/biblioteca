from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import widgets

from .models import *


class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']
        labels = {
            'nombre': 'Nombre del autor: ',
            'apellidos': 'Apellidos del autor: ',
            'nacionalidad': 'Nacionalidad del autor: ',
            'descripcion': 'Pequeña descripción: ',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'true',
                    'placeholder': 'Ingresa el nombre del autor...',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa los apellidos del autor...',
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la nacionalidad del autor...',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa la descripción del autor...',
                }
            )
        }


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['titulo', 'autor_id', 'fecha_publicacion']
        labels = {
            'titulo': ' Titulo del libro',
            'autor_id': 'Autor(es) del libro',
            'fecha_publicacion': 'Fecha de publicación del libro',
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese titulo del libro'
                }
            ),
            'autor_id': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(LibroForm, self).__init__(*args, **kwargs)
        self.fields['fecha_publicacion'].widget.attrs['readonly'] = True
