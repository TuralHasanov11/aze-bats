from django.shortcuts import render
from bats import models
from django.core import paginator
from django.db.models import Prefetch
from django.utils import translation

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
    bat_attributes = models.SpeciesAttributes.objects.filter(language=translation.get_language())
    prefetch = Prefetch('species_attributes', queryset=bat_attributes)
    bat = models.Species.objects.select_related("genus").prefetch_related('species_images', prefetch).get(slug=slug)
    bat.species_attributes_result = bat.species_attributes.all().first()
    return render(request, "bats/detail.html", {"bat": bat})