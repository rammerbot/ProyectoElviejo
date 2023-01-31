from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL amigable")
    vivible = models.BooleanField(verbose_name="visible")
    position = models.IntegerField(default= 0, verbose_name="Posision")
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el ")
    update_at = models.DateField(auto_now=True, verbose_name="Actualizado el ")

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"

    def __str__(self):
        return self.title