from django.shortcuts import render
from bats import models
from django.core import paginator


def index(request):
    genusSlug = request.GET.get("genus", None)

    if genusSlug:
        bats = models.Species.objects.filter(genus__slug=genusSlug)
    else:
        bats = models.Species.objects.all()
    
    pagination = paginator.Paginator(bats, 1)
    pageNumber = request.GET.get('page')
    bats = pagination.get_page(pageNumber)

    genus = models.Genus.objects.all()
    return render(request, "bats/index.html", {"bats": bats, "genus": genus})


def detail(request, slug:str):
    bat = models.Species.objects.select_related("genus").prefetch_related('species_images').get(slug=slug)
    return render(request, "bats/detail.html", {"bat": bat})