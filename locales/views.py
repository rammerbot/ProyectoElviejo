from django.shortcuts import render, get_object_or_404
from locales.models import Local

def locales(request):

    locales = Local.objects.all()

    return render(request,"locales/local.html", {
        "titulo":"Local",
        "locales":locales
    } )
# Create your views here.

def local_detalle(request, local_id):
    
    local = Local.objects.filter(id = local_id)
    
    return render(request, "locales/locales.html",{
        "local":local
    })