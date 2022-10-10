from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from bats import models as batModels
from activities import models as activityModels
from base import models as baseModels
from django.views.decorators import http
from django.contrib.auth import decorators as authDecorators
from administration import forms
from django.contrib import messages
from django.utils.translation import gettext as _


@authDecorators.login_required
@http.require_GET
def dashboard(request):
    return render(request, "administration/dashboard.html")


@authDecorators.login_required
@http.require_GET
def batList(request):
    bats = batModels.Species.objects.select_related("genus")
    return render(request, "administration/bats/list.html", {"bats":bats})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST"])
def batCreate(request):
    if request.POST:
        form = forms.BatSpeciesCreateForm(request.POST, request.FILES)
        attributes_formset = forms.SpeciesAttributesFormset(data=request.POST, files=request.FILES)
        images_formset = forms.SpeciesImageFormset(data=request.POST, files=request.FILES)
        if form.is_valid() and attributes_formset.is_valid() and images_formset.is_valid():
            bat = form.save()
            attributes = attributes_formset.save(commit=False)
            images = images_formset.save(commit=False)
            for attr in attributes:
                attr.species = bat
                attr.save()
            for img in images:
                img.species = bat
                img.save()
            messages.success(request, _("Bat added!"))
            return redirect("administration:bat-list")
        messages.error(request, _("Bat cannot be added!"))
        return render(request, "administration/bats/create.html", {"form": form, "attributes_formset":attributes_formset, "images_formset":images_formset})
    form = forms.BatSpeciesCreateForm()
    attributes_formset = forms.SpeciesAttributesFormset()
    images_formset = forms.SpeciesImageFormset()
    return render(request, "administration/bats/create.html", {"form": form, "attributes_formset":attributes_formset, "images_formset":images_formset})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST", "DELETE"])
def batUpdateDelete(request, id):
    if request.method == "DELETE":
        batModels.Species.objects.get(id=id).delete()
        return HttpResponse(f"Species {id} deleted")

    bat = batModels.Species.objects.prefetch_related('species_images').get(id=id)
    if request.POST:
        form = forms.BatSpeciesUpdateForm(instance=bat, data=request.POST, files=request.FILES)
        attributes_formset = forms.SpeciesAttributesFormset(instance=bat, data=request.POST, files=request.FILES)
        images_formset = forms.SpeciesImageFormset(instance=bat, data=request.POST, files=request.FILES)
        if form.is_valid() and attributes_formset.is_valid() and images_formset.is_valid():
            bat = form.save()
            attributes_formset.save()
            images_formset.save()
            messages.success(request, _("Bat updated!"))
            return redirect("administration:bat-update-delete", id=id)
        messages.error(request, _("Bat cannot be updated!"))
        return render(request, "administration/bats/update.html", {"form": form, "bat":bat, "attributes_formset":attributes_formset, "images_formset":images_formset})
    form = forms.BatSpeciesUpdateForm(instance=bat)
    attributes_formset = forms.SpeciesAttributesFormset(instance=bat)
    images_formset = forms.SpeciesImageFormset(instance=bat)
    return render(request, "administration/bats/update.html", {"form": form, "bat":bat, "attributes_formset":attributes_formset, "images_formset":images_formset})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST"])
def authorListCreate(request):
    if request.POST:
        form = forms.AuthorForm(data=request.POST, files=request.FILES)
        attributes_formset = forms.AuthorAttributesFormset(data=request.POST, files=request.FILES)
        if form.is_valid() and attributes_formset.is_valid():
            author = form.save()
            attributes = attributes_formset.save(commit=False)
            for attr in attributes:
                attr.author = author
                attr.save()
            messages.success(request, _("Researcher added!"))
            return redirect("administration:author-list-create")
        messages.error(request, _("Researcher cannot be added!"))
        return render(request, "administration/authors/list.html", {"form": form, "attributes_formset":attributes_formset})
    form = forms.AuthorForm()
    attributes_formset = forms.AuthorAttributesFormset()
    authors = baseModels.Author.objects.prefetch_related('author_attributes').all()
    return render(request, "administration/authors/list.html", {"form": form, "authors":authors, "attributes_formset":attributes_formset})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST", "DELETE"])
def authorUpdateDelete(request, id):
    if request.method == "DELETE":
        baseModels.Author.objects.get(id=id).delete()
        return HttpResponse(f"Author {id} deleted")

    author = get_object_or_404(baseModels.Author, id=id)
    if request.POST:
        form = forms.AuthorForm(instance=author, data=request.POST, files=request.FILES)
        attributes_formset = forms.AuthorAttributesFormset(data=request.POST, files=request.FILES)
        if form.is_valid() and attributes_formset.is_valid():
            author = form.save()
            attributes_formset.save()
            messages.success(request, _("Researcher updated!"))
            return redirect("administration:author-update-delete", id=id)
        messages.error(request, _("Researcher cannot be updated!"))
        return render(request, "administration/authors/update.html", {"form": form, "author":author, "attributes_formset":attributes_formset})
    form = forms.AuthorForm(instance=author)
    attributes_formset = forms.AuthorAttributesFormset(instance=author)
    return render(request, "administration/authors/update.html", {"form": form, "author":author, "attributes_formset":attributes_formset})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST"])
def articleListCreate(request):
    if request.POST:
        form = forms.ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Article added!"))
            return redirect("administration:article-list-create")
        messages.error(request, _("Article cannot be added!"))
        return render(request, "administration/articles/list.html", {"form": form})
    form = forms.ArticleForm()
    articles = baseModels.Article.objects.all()
    return render(request, "administration/articles/list.html", {"form": form, "articles":articles})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST", "DELETE"])
def articleUpdateDelete(request, id):
    if request.method == "DELETE":
        baseModels.Article.objects.get(id=id).delete()
        return HttpResponse(f"Article {id} deleted")

    article = get_object_or_404(baseModels.Article, id=id)
    if request.POST:
        form = forms.ArticleForm(instance=article, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Article updated!"))
            return redirect("administration:article-update-delete", id=id)
        messages.error(request, _("Article cannot be updated!"))
        return render(request, "administration/articles/update.html", {"form": form, "article":article})
    form = forms.ArticleForm(instance=article)
    return render(request, "administration/articles/update.html", {"form": form, "article":article})


@authDecorators.login_required
@http.require_GET
def projectList(request):
    projects = activityModels.Project.objects.all()
    return render(request, "administration/projects/list.html", {"projects":projects})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST"])
def projectCreate(request):
    if request.POST:
        form = forms.ProjectCreateForm(data=request.POST, files=request.FILES)
        attributes_formset = forms.ProjectAttributesFormset(data=request.POST, files=request.FILES)
        images_formset = forms.ProjectImageFormset(data=request.POST, files=request.FILES)
        if form.is_valid() and attributes_formset.is_valid() and images_formset.is_valid():
            project = form.save()
            attributes = attributes_formset.save(commit=False)
            images = images_formset.save(commit=False)
            for attr in attributes:
                attr.project = project
                attr.save()
            for img in images:
                img.project = project
                img.save()
            messages.success(request, _("Project added!"))
            return redirect("administration:project-list")
        messages.error(request, _("Project cannot be added!"))
        return render(request, "administration/projects/create.html", {"form": form, "attributes_formset":attributes_formset, "images_formset":images_formset})
    form = forms.ProjectCreateForm()
    attributes_formset = forms.ProjectAttributesFormset()
    images_formset = forms.ProjectImageFormset()
    return render(request, "administration/projects/create.html", {"form": form, "attributes_formset":attributes_formset, "images_formset":images_formset})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST", "DELETE"])
def projectUpdateDelete(request, id):
    if request.method == "DELETE":
        activityModels.Project.objects.get(id=id).delete()
        return HttpResponse(f"Project {id} deleted")

    project = activityModels.Project.objects.prefetch_related('project_images').get(id=id)
    if request.POST:
        form = forms.ProjectUpdateForm(instance=project, data=request.POST, files=request.FILES)
        attributes_formset = forms.ProjectAttributesFormset(instance=project, data=request.POST, files=request.FILES)
        images_formset = forms.ProjectImageFormset(instance=project, data=request.POST, files=request.FILES)
        if form.is_valid() and attributes_formset.is_valid() and images_formset.is_valid():
            project = form.save()
            attributes_formset.save()
            images_formset.save()
            messages.success(request, _("Project updated!"))
            return redirect("administration:project-update-delete", id=id)
        messages.success(request, _("Project cannot be updated!"))
        return render(request, "administration/projects/update.html", {"form": form, "attributes_formset":attributes_formset, "images_formset":images_formset})
    form = forms.ProjectUpdateForm(instance=project)
    attributes_formset = forms.ProjectAttributesFormset(instance=project)
    images_formset = forms.ProjectImageFormset(instance=project)
    return render(request, "administration/projects/update.html", {"form": form, "attributes_formset":attributes_formset, "images_formset":images_formset})


@authDecorators.login_required
@http.require_GET
def visitList(request):
    visits = activityModels.SiteVisit.objects.all()
    return render(request, "administration/visits/list.html", {"visits":visits})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST"])
def visitCreate(request):
    if request.POST:
        form = forms.SiteVisitCreateForm(data=request.POST, files=request.FILES)
        attributes_formset = forms.SiteVisitAttributesFormset(data=request.POST, files=request.FILES)
        images_formset = forms.SiteVisitImageFormset(data=request.POST, files=request.FILES)
        if form.is_valid() and attributes_formset.is_valid() and images_formset.is_valid():
            visit = form.save()
            attributes = attributes_formset.save(commit=False)
            images = images_formset.save(commit=False)
            for attr in attributes:
                attr.site_visit = visit
                attr.save()
            for img in images:
                img.site_visit = visit
                img.save()
            messages.success(request, _("Site Visit added!"))
            return redirect("administration:visit-list")
        messages.success(request, _("Site Visit cannot be added!"))
        return render(request, "administration/visits/create.html", {"form": form, "attributes_formset":attributes_formset, "images_formset":images_formset})
    form = forms.SiteVisitCreateForm()
    attributes_formset = forms.SiteVisitAttributesFormset()
    images_formset = forms.SiteVisitImageFormset()
    return render(request, "administration/visits/create.html", {"form": form, "attributes_formset":attributes_formset, "images_formset":images_formset})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST", "DELETE"])
def visitUpdateDelete(request, id):
    if request.method == "DELETE":
        activityModels.SiteVisit.objects.get(id=id).delete()
        return HttpResponse(f"SiteVisit {id} deleted")

    visit = activityModels.SiteVisit.objects.prefetch_related('site_visit_images').get(id=id)
    if request.POST:
        form = forms.SiteVisitUpdateForm(instance=visit, data=request.POST, files=request.FILES)
        attributes_formset = forms.SiteVisitAttributesFormset(instance=visit, data=request.POST, files=request.FILES)
        images_formset = forms.SiteVisitImageFormset(instance=visit, data=request.POST, files=request.FILES)
        if form.is_valid() and attributes_formset.is_valid() and images_formset.is_valid():
            visit = form.save()
            attributes_formset.save()
            images_formset.save()
            messages.success(request, _("Site Visit updated!"))
            return redirect("administration:visit-update-delete", id=id)
        messages.success(request, _("Site Visit cannot be updated!"))
        return render(request, "administration/visits/update.html", {"form": form, "visit":visit, "attributes_formset":attributes_formset, "images_formset":images_formset})
    
    form = forms.SiteVisitUpdateForm(instance=visit)
    attributes_formset = forms.SiteVisitAttributesFormset(instance=visit)
    images_formset = forms.SiteVisitImageFormset(instance=visit)
    return render(request, "administration/visits/update.html", {"form": form, "visit":visit, "attributes_formset":attributes_formset, "images_formset":images_formset}) 

