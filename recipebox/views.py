from django.shortcuts import render
from recipebox.models import NewsItem

def index(request):
    html = 'index.html'

    news = NewsItem.objects.all()

    return render(request, html, {'data': news})