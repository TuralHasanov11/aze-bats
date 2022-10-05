from django.shortcuts import render, get_object_or_404
from activities import models
from django.core import paginator

def projects(request):
    pagination = paginator.Paginator(models.Project.objects.all(), 10)
    pageNumber = request.GET.get('page')
    projects = pagination.get_page(pageNumber)

    return render(request, "activities/projects.html", {"projects": projects})


def project(request, id):
    project = get_object_or_404(models.Project, id=id)
    return render(request, "activities/project.html", {"project": project})


def visits(request):
    pagination = paginator.Paginator(models.SiteVisit.objects.all(), 10)
    pageNumber = request.GET.get('page')
    visits = pagination.get_page(pageNumber)

    return render(request, "activities/visits.html", {"visits": visits})


def visit(request):
    visit = get_object_or_404(models.SiteVisit, id=id)
    return render(request, "activities/visit.html", {"visit": visit})
