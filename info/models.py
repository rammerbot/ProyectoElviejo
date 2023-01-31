from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Info(models.Model):
    
    titulo = models.CharField(max_length=50, verbose_name="Titulo")
    descripcion = RichTextField(verbose_name="contenido")
    imagenes = models.ImageField(default="null", verbose_name="imagen", upload_to="media/articles")
    fecha_creacion = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    fecha_modificacion =models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualizacion")

    class Meta:
        verbose_name="Empresa"

    def __str__(self):
        return self.titulo
    