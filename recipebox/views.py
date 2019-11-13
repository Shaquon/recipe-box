from django.shortcuts import render, HttpResponseRedirect, reverse
from recipebox.models import RecipeItem
from recipebox.models import Author
from recipebox.forms import AuthorAdd, NewsItemAdd_, LoginForm
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    html = 'index.html'

    recipes = RecipeItem.objects.all()

    return render(request, html, {'data': recipes})


@login_required
def recipe_item_view(request, key_id):
    html = 'item_page.html'

    recipe = RecipeItem.objects.get(pk=key_id)

    return render(request, html, {'data': recipe})


@login_required
def author_view(request, key_id):

    html = 'author_page.html'

    author = Author.objects.get(pk=key_id)

    items = RecipeItem.objects.all().filter(author=author)

    return render(request, html, {
        'author': author,
        'recipes': items
        })


@login_required
def add_author_view(request):

    html = "author_add.html"

    if request.method == 'POST':

        form = AuthorAdd(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(name=data['name'], bio=data['bio'])

            return HttpResponseRedirect(reverse('homepage'))
    form = AuthorAdd()
    return render(request, html, {'form': form})


@login_required
def add_item_view(request):
    html = "item_add.html"
    if request.method == 'POST':
        form = NewsItemAdd_(request.POST)
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
    form = NewsItemAdd_()
    return render(request, html, {'form': form})


def login_view(request):
    html = "item_add.html"

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))

    form = LoginForm()

    return render(request, html, {form: form})

# simple form
# def add_item_view(request):
#     html = "item_add.html"

#     if request.method == 'POST':

#         form = NewsItemAdd(request.POST)

#         if form.is_valid():

#             data = form.cleaned_data

#             RecipeItem.objects.create(
#                 title=data['title'],
#                 author=data['author'],
#                 description=data['description'],
#                 prep_time=data['prep_time'],
#                 instructions=data['instructions'],
#                 post_date=timezone.now()
#             )
#             return HttpResponseRedirect(reverse('homepage'))

#     form = NewsItemAdd()

#     return render(request, html, {'form': form})
