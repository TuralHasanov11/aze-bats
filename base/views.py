from django.shortcuts import render
from django.core import paginator
from base import models
from bats import models as batModels
from activities import models as activityModels


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

def articles(request):
    pagination = paginator.Paginator(models.Article.objects.all(), 30)
    pageNumber = request.GET.get('page')
    articles = pagination.get_page(pageNumber)

    return render(request, "base/articles.html", {"articles": articles})
