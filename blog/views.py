from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category

# Create your views here.

def  list(request):

    articles = Article.objects.all().order_by("create_at")

    return render(request, "articles/list.html",{
        "title":"Articulos",
        "articulos":articles,
    })

def category(request, category_id):
   
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category_id)
    
    return render(request, 'categories/category.html',{
        "category":category,
        "articulos":articles,
    }) 

def article(request, article_id):
    
    article = get_object_or_404(Article, id = article_id)


    return render(request, 'articles/detail.html',{
        "article":article,

    })
