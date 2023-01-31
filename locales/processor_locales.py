from locales.models import Local

def get_mapas(request):

    locales = Local.objects.values_list("id", "local")

    return {
        "locales_list" : locales,

    }