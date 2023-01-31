from page.models import Page

def get_pages(request):

    pages = Page.objects.filter(vivible=True).order_by("position").values_list("id", "title", "slug")

    return {
        "pages" : pages
    }