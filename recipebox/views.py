from django.shortcuts import render, HttpResponseRedirect, reverse
from recipebox.models import RecipeItem
from recipebox.models import Author
from recipebox.forms import AuthorAdd, NewsItemAdd
from django.utils import timezone


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


def add_author_view(request):

    html = "author_add.html"

    if request.method == 'POST':

        form = AuthorAdd(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(name=data['name'])

        return HttpResponseRedirect(reverse('homepage'))
    form = AuthorAdd()
    return render(request, html, {'form': form})


def add_item_view(request):
    html = "item_add.html"

    if request.method == 'POST':

        form = NewsItemAdd(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            RecipeItem.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                prep_time=data['prep_time'],
                instructions=data['instructions'],
                post_date=timezone.now()
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = NewsItemAdd()

    return render(request, html, {'form': form})
