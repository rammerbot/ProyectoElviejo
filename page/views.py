from django.shortcuts import render
from .models import Page

# Create your views here.


def page(request, url):
    
    page = Page.objects.get(slug=url)

    return render(request, "pages/page.html", {
        "page": page
        
    })
