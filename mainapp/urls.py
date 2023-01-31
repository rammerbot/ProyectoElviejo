from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="Inicio"),
    path("inicio/", views.index, name="Inicio"),
    path("carrusel/", views.carrusel, name="Carrusel")


]