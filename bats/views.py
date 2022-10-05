from django.shortcuts import render
from bats import models

def index(request):
    bats = models.Species.objects.all()
    return render(request, "bats/index.html", {"bats": bats})


def detail(request, slug:str):
    bat = models.Species.objects.select_related("genus.family").get(slug=slug)
    return render(request, "bats/detail.html", {"bat": bat})