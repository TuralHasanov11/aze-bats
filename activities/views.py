from django.shortcuts import render

def projects(request):
    return render(request, "base/index.html")


def project(request):
    return render(request, "base/project.html")


def visits(request):
    return render(request, "base/visits.html")


def visit(request):
    return render(request, "base/visit.html")
