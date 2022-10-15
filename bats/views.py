from django.shortcuts import render
from bats import models
from django.core import paginator
from django.db.models import Prefetch
from django.utils import translation
from django.views.decorators import http

@http.require_GET
def index(request):
    genusSlug = request.GET.get("genus", None)

    if genusSlug:
        bats = models.Species.objects.filter(genus__slug=genusSlug)
    else:
        bats = models.Species.objects.all()
    
    pagination = paginator.Paginator(bats, 10)
    pageNumber = request.GET.get('page')
    bats = pagination.get_page(pageNumber)

    genus = models.Genus.objects.all()
    return render(request, "bats/index.html", {"bats": bats, "genus": genus})


@http.require_GET
def detail(request, slug:str):
    bat_attributes = models.SpeciesAttributes.objects.filter(language=translation.get_language())
    bat_red_book = models.SpeciesRedBook.objects.filter(language=translation.get_language())
    prefetch_species_attributes = Prefetch('species_attributes', queryset=bat_attributes)
    prefetch_bat_red_book = Prefetch('species_red_book', queryset=bat_red_book)
    bat = models.Species.objects.select_related("genus").prefetch_related('species_images', prefetch_species_attributes, prefetch_bat_red_book).get(slug=slug)
    bat.species_attributes_result = bat.species_attributes.all().first()
    bat.species_red_book_result = bat.species_red_book.all().first()
    return render(request, "bats/detail.html", {"bat": bat})