from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from recipebox.models import RecipeItem
from recipebox.models import Author
from recipebox.forms import AuthorAdd, NewsItemAdd_, LoginForm, EditRecipeForm
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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

    favorites = author.favorite.all()

    return render(request, html, {
        'author': author,
        'recipes': items,
        'favorites': favorites
        })


@login_required
def chef_add_view(request):
    html = "generic_form.html"
    if request.user.is_staff == True:
        if request.method == 'POST':
            form = ChefAddForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                u = User.objects.create_user(
                    username=data['name']
                )
                Author.objects.create(
                    user=u,
                    name=data['name'],
                    bio=data.get('bio')
                    )
                return HttpResponseRedirect(reverse('additem'))
    else:
        return HttpResponse("Nah homie.  You don't have the proper credentials")
    form = AuthorAdd()
    return render(request, html, {'form': form})


def add_author_view(request):
    html = "author_add.html"
    if request.method == 'POST':
        form = AuthorAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data['name'],
                password=data['password']
            )
            Author.objects.create(
                user=u,
                name=data['name'],
                bio=data.get('bio')
            )
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
    html = "log_in.html"
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
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                    )

    form = LoginForm()

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def edit_recipe_view(request,id):
    html = "generic_form.html"
    instance = RecipeItem.objects.get(id=id)
    logged_in = request.user
    print(logged_in)
    print(instance.author)
    if logged_in.is_staff == True or logged_in == instance.author.user:
        if request.method == "POST":
            form = EditRecipeForm(request.POST, instance=instance)
            form.save()
            return HttpResponseRedirect(reverse('homepage'))
    else:
        return HttpResponse("You can't do that")
    form = EditRecipeForm(instance=instance)
    return render(request, html, {'form': form})


@login_required
def favorited(request,id):
    current_user = request.user.author
    desired_recipe = RecipeItem.objects.get(id=id)

    current_user.favorite.add(desired_recipe)
    return HttpResponseRedirect(request.META.get('HTTP_REFFERER', '/'))


def unfavorited(request,id):
    current_user = request.user.author
    desired_recipe = RecipeItem.objects.get(id=id)

    current_user.favorite.remove(desired_recipe)
    return HttpResponseRedirect(request.META.get('HTTP_REFFERER', '/'))


def favorite_view(request):
    pass