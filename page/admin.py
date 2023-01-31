from django.contrib import admin
from .models import Page

# Register your models here.


admin.site.register(Page)

header = "Gestor de sitio Web \"El Viejo\""
title = "El Viejo"
subtitulo = "Panel de Administracion"

admin.site.site_header = header
admin.site.site_title = title
admin.site.index_title = subtitulo