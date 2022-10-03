from django.shortcuts import render

def projects(request):
    return render(request, "activities/index.html")


def project(request):
    return render(request, "activities/project.html")


def visits(request):
    return render(request, "activities/visits.html")


def visit(request):
    return render(request, "activities/visit.html")
