from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.usuario.models import Usuario


class FormularioUsuario(forms.ModelForm):
    """
    Formulario de registro de un usuario en la BD.

    Variables:
        - password1: Contraseña
        - password2: Verificación de contraseña
    """

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label='Contraseña de confirmación', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Repite tu contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email', 'username', 'nombres', 'apellidos')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa tu nombre'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa tus apellidos'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa tu nombre de usuario'
                }
            )
        }

    def clean_password2(self):
        """
        Validación de las contraseñas.

        Método que valida que sean iguales las contraseñas, antes de guardar en la BD.

        Excepciones:
            - ValidatoinError -- Cuando las contraseñas no son iguales
        """

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            return forms.ValidationError('Las constraseñas no coincide')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
