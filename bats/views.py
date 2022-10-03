from django.shortcuts import render

def index(request):
    return render(request, "bats/index.html")


def detail(request, slug:str):
    return render(request, "bats/detail.html")