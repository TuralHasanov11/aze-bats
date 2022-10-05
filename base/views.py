from django.shortcuts import render
from django.core import paginator
from base import models

def index(request):
    authors = models.Author.objects.all()
    return render(request, "base/index.html", {"authors": authors})

def articles(request):
    pagination = paginator.Paginator(models.Article.objects.all(), 30)
    pageNumber = request.GET.get('page')
    articles = pagination.get_page(pageNumber)

    return render(request, "base/articles.html", {"articles": articles})
