from django.db import models
from ckeditor.fields import RichTextField



class Local(models.Model):

    local = models.CharField(max_length= 50, verbose_name="Local")
    descripcion = RichTextField(verbose_name= "Descripcion")
    ubicacion = models.CharField(max_length=220, verbose_name="Direccion")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="media/articles")
    mapa = models.URLField(verbose_name="Google.maps")


    class Meta:
        verbose_name="Local"
        verbose_name_plural = "Locales"

    def __str__(self):
        return self.local

# Create your models here.
