from django.shortcuts import render
from recipebox.models import RecipeItem
from recipebox.models import Author


def index(request):
    html = 'index.html'

    recipes = RecipeItem.objects.all()

    return render(request, html, {'data': recipes})


def recipe_item_view(request, key_id):
    html = 'item_page.html'

    recipe = RecipeItem.objects.get(pk=key_id)

    return render(request, html, {'data': recipe})


def author_view(request, key_id):

    html = 'author_page.html'

    author = Author.objects.get(pk=key_id)

    items = RecipeItem.objects.all().filter(author=author)

    return render(request, html, {
        'author': author,
        'recipes': items
        })
