from django.shortcuts import render
from django.core import paginator
from base import models
from bats import models as batModels

def index(request):
    authors = models.Author.objects.all()
    bats = batModels.Species.objects.all()[:14]
    batCount = batModels.Species.objects.count()
    projectCount = batModels.Species.objects.count()
    visitCount = batModels.Species.objects.count()
    batsFormatted = []
    if bats:
        for i in range(0, len(bats), 7):
            batsFormatted[i].append(bats[i:i + 7])
        print(batsFormatted)
    return render(request, "base/index.html", {"authors": authors, "batCount": batCount, "batsFormatted":batsFormatted, "projectCount":projectCount, "visitCount":visitCount})

def articles(request):
    pagination = paginator.Paginator(models.Article.objects.all(), 30)
    pageNumber = request.GET.get('page')
    articles = pagination.get_page(pageNumber)

    return render(request, "base/articles.html", {"articles": articles})
