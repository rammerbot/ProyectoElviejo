from django.urls import path
from . import views

urlpatterns = [

    path("locales/", views.locales, name="local_list"),
    path("local/<int:local_id>", views.local_detalle ,name="local"),

]