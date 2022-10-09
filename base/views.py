from django.shortcuts import render
from django.core import paginator
from base import models
from bats import models as batModels
from activities import models as activityModels
from django.views.decorators import http

@http.require_GET
def index(request):
    authors = models.Author.objects.all()
    bats = batModels.Species.objects.all()[:12]
    batCount = batModels.Species.objects.count()
    projectCount = batModels.Species.objects.count()
    visits = activityModels.SiteVisit.objects.all()[:4]
    projects = activityModels.Project.objects.all()[:4]
    visitCount = batModels.Species.objects.count()
            
    return render(request, "base/index.html", {
        "authors": authors, 
        "batCount": batCount, 
        "bats":bats, 
        "projectCount":projectCount, 
        "visitCount":visitCount,
        "projects":projects,
        "visits":visits
    })

@http.require_GET
def articles(request):
    pagination = paginator.Paginator(models.Article.objects.all(), 30)
    pageNumber = request.GET.get('page')
    articles = pagination.get_page(pageNumber)

    return render(request, "base/articles.html", {"articles": articles})

@http.require_GET
def search(request):
    query = request.GET.get('search', None)

    if query:
        projects = activityModels.Project.objects.filter(name__contains=query)
        visits = activityModels.SiteVisit.objects.filter(name__contains=query)
        bats = batModels.Species.objects.filter(name__contains=query)

    return render(request, "base/search.html", {"visits": projects, "projects": visits, "bats":bats})