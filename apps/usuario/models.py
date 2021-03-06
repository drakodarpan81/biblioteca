from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres, apellidos, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')

        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            nombres=nombres,
            apellidos=apellidos)

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email, username, nombres, apellidos, password):
        usuario = self.create_user(
            email,
            username=username,
            nombres=nombres,
            apellidos=apellidos,
            password=password
        )

        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    username = models.CharField(
        _("Nombre de usuario"), max_length=100, unique=True)
    email = models.EmailField(_("Correo Electrónico"),
                              max_length=254, unique=True)
    nombres = models.CharField(
        _("Nombres"), max_length=200, blank=True, null=True)
    apellidos = models.CharField(
        _("Apellidos"), max_length=200, blank=True, null=True)
    imagen = models.ImageField(
        _("Imagen de perfil"), upload_to='perfil/', max_length=200, blank=True, null=True)
    usuario_activo = models.BooleanField(
        _("Usuario Activo/Inactivo"), default=True)
    usuario_administrador = models.BooleanField(
        _("Admin Activo/Inactivo"), default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.username} - {self.apellidos}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador
