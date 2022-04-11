from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm

from django.views.generic.edit import FormView
from .forms import FormularioLogin

# Create your views here.


def logout_request(request):
    logout(request)
    # messages.success(request, 'Se cerro la sesión de manera correcta...')
    return redirect('login')


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')


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
