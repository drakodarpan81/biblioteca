import json
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.core import serializers
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView

from django.views.generic.edit import FormView

from apps.usuario.models import Usuario
from .forms import FormularioLogin
from apps.usuario.forms import FormularioUsuario

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


def logout_request(request):
    logout(request)
    # messages.success(request, 'Se cerro la sesión de manera correcta...')
    return redirect('login')


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    form = AuthenticationForm()
    return render(request=request, template_name='login.html', context={"login_form": form})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    

class InicioListadoView(TemplateView):
    template_name = "usuarios/listar_usuarios.html"

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "usuarios/listar_usuarios.html"
    context_object_name = 'usuarios'

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)

    def get(self, request, *args, **kwargs):
        if is_ajax(request=request):
            data = serializers.serialize('json', self.get_queryset(),)
            return HttpResponse(data)
        else:
            return redirect('usuarios:listar_usuarios')


class RegistrarUsuario(LoginRequiredMixin, CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                nombres=form.cleaned_data['nombres'],
                apellidos=form.cleaned_data['apellidos']
            )
            nuevo_usuario.set_password(form.cleaned_data['password1'])
            nuevo_usuario.save()
            return redirect('usuarios:listar_usuarios')
        else:
            return redirect(request, self.template_name, {'form': form})
