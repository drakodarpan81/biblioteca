from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Autor(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    nombre = models.CharField(_("Nombre"), max_length=200, blank=False, null=False)
    apellidos = models.CharField(_("Apellidos"), max_length=200, blank=False, null=False)
    nacionalidad = models.CharField(_("Nacionalidad"), max_length=100, blank=False, null=False)
    descripcion = models.TextField(_("Descripcion"), blank=False, null=False)
    fecha_creacion = models.DateField(_("Fecha de creación"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Autor")
        verbose_name_plural = _("Autores")
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Autor_detail", kwargs={"pk": self.pk})

class Libro(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    titulo = models.CharField(_("Titulo"), max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField(_("Fecha de publicación"), blank=False, null=False)
    autor_id = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField(_("Fecha de creación"), auto_now=True, auto_now_add=False)
    

    class Meta:
        verbose_name = _("Libro")
        verbose_name_plural = _("Libros")
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("Libro_detail", kwargs={"pk": self.pk})
