from django.shortcuts import render
from recipebox.models import RecipeItem
from recipebox.models import Author


def index(request):
    html = 'index.html'

    recipes = RecipeItem.objects.all()

    return render(request, html, {'data': recipes})


def recipe_item_view(request):
    html = 'item_page.html'

    recipes = RecipeItem.objects.all()

    return render(request, html, {'data': recipes})


def author_add_view(request, key_id):

    html = 'author_page.html'

    author = Author.objects.get(pk=key_id)

    items = RecipeItem.objects.all().filter(author=author)

    return render(request, html, {
        'author': author,
        'recipes': items
        })
