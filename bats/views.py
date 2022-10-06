from django.shortcuts import render
from bats import models

def index(request):
    bats = models.Species.objects.all()
    genus = models.Genus.objects.all()
    return render(request, "bats/index.html", {"bats": bats, "genus": genus})


def detail(request, slug:str):
    bat = models.Species.objects.select_related("genus").get(slug=slug)
    return render(request, "bats/detail.html", {"bat": bat})