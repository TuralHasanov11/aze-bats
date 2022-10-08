from django.shortcuts import render
from activities import models
from django.core import paginator
from django.db.models import Prefetch
from django.utils import translation

def projects(request):
    pagination = paginator.Paginator(models.Project.objects.all(), 10)
    pageNumber = request.GET.get('page')
    projects = pagination.get_page(pageNumber)

    return render(request, "activities/projects.html", {"projects": projects})


def project(request, slug):
    project_attributes = models.ProjectAttributes.objects.filter(language=translation.get_language())
    prefetch = Prefetch('project_attributes', queryset=project_attributes)
    project = models.Project.objects.prefetch_related("project_images", prefetch).get(slug=slug)
    project.project_attributes_result = project.project_attributes.all().first()
    return render(request, "activities/project.html", {"project": project})


def visits(request):
    pagination = paginator.Paginator(models.SiteVisit.objects.all(), 10)
    pageNumber = request.GET.get('page')
    visits = pagination.get_page(pageNumber)

    return render(request, "activities/visits.html", {"visits": visits})


def visit(request, slug):
    visit_attributes = models.SiteVisitAttributes.objects.filter(language=translation.get_language())
    prefetch = Prefetch('site_visit_attributes', queryset=visit_attributes)
    visit = models.SiteVisit.objects.prefetch_related("site_visit_images", prefetch).get(slug=slug)
    visit.site_visit_attributes_result = visit.site_visit_attributes.all().first()
    return render(request, "activities/visit.html", {"visit": visit})
