from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripcion")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

class Article(models.Model):
    
    title = models.CharField(max_length=100, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default="null", verbose_name="imagen", upload_to="media/articles")
    public = models.BooleanField(verbose_name="Visible")
    user = models.ForeignKey(User, verbose_name="Usuario",editable=False, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name="Categorias", blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Ultima modificacion: ")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        return self.title
