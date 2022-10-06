from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from bats import models as batModels
from activities import models as activityModels
from base import models as baseModels
from django.views.decorators import http
from django.contrib.auth import decorators as authDecorators
from administration import forms

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
        form = forms.CreateBatSpeciesForm(request.POST, request.FILES)
        if form.is_valid():
            bat = form.save()
            if request.FILES['images']:
                for img in request.FILES.getlist('images'):
                    batModels.SpeciesImage.objects.create(image=img, species=bat)
            return redirect("administration:bat-list")
        return render(request, "administration/bats/create.html", {"form": form})
    else:
        form = forms.CreateBatSpeciesForm()
        return render(request, "administration/bats/create.html", {"form": form})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST", "DELETE"])
def batUpdateDelete(request, id):
    if request.method == "DELETE":
        batModels.Species.objects.get(id=id).delete()
        return HttpResponse(f"Species {id} deleted")

    bat = batModels.Species.objects.prefetch_related('species_images').get(id=id)
    if request.POST:
        form = forms.UpdateBatSpeciesForm(instance=bat, data=request.POST, files=request.FILES)
        if form.is_valid():
            bat = form.save()
            if request.FILES['images']:
                for img in request.FILES.getlist('images'):
                    batModels.SpeciesImage.objects.create(image=img, species=bat)
            return redirect("administration:bat-update-delete", id=id)
        return render(request, "administration/bats/update.html", {"form": form, "bat":bat})
    form = forms.UpdateBatSpeciesForm(instance=bat)
    return render(request, "administration/bats/update.html", {"form": form, "bat":bat})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST"])
def authorListCreate(request):
    if request.POST:
        form = forms.CreateAuthorForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("administration:author-list-create")
        return render(request, "administration/authors/list.html", {"form": form})
    form = forms.CreateAuthorForm()
    authors = baseModels.Author.objects.all()
    return render(request, "administration/authors/list.html", {"form": form, "authors":authors})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST", "DELETE"])
def authorUpdateDelete(request, id):
    if request.method == "DELETE":
        baseModels.Author.objects.get(id=id).delete()
        return HttpResponse(f"Author {id} deleted")

    author = get_object_or_404(baseModels.Author, id=id)
    if request.POST:
        form = forms.UpdateAuthorForm(instance=author, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("administration:author-update-delete", id=id)
        return render(request, "administration/authors/update.html", {"form": form, "author":author})
    form = forms.UpdateAuthorForm(instance=author)
    return render(request, "administration/authors/update.html", {"form": form, "author":author})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST"])
def articleListCreate(request):
    if request.POST:
        form = forms.ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("administration:article-list-create")
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
            return redirect("administration:article-update-delete", id=id)
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
        form = forms.ProjectCreateForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            if request.FILES['images']:
                for img in request.FILES.getlist('images'):
                    activityModels.ProjectImage.objects.create(image=img, project=project)
            return redirect("administration:project-list")
        return render(request, "administration/projects/create.html", {"form": form})
    else:
        form = forms.ProjectCreateForm()
        return render(request, "administration/projects/create.html", {"form": form})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST", "DELETE"])
def projectUpdateDelete(request, id):
    if request.method == "DELETE":
        activityModels.Project.objects.get(id=id).delete()
        return HttpResponse(f"Project {id} deleted")

    project = activityModels.Project.objects.prefetch_related('project_images').get(id=id)
    if request.POST:
        form = forms.ProjectUpdateForm(instance=project, data=request.POST, files=request.FILES)
        if form.is_valid():
            project = form.save()
            if request.FILES['images']:
                for img in request.FILES.getlist('images'):
                    activityModels.ProjectImage.objects.create(image=img, project=project)
            return redirect("administration:project-update-delete", id=id)
        return render(request, "administration/projects/update.html", {"form": form, "project":project})
    form = forms.ProjectUpdateForm(instance=project)
    return render(request, "administration/projects/update.html", {"form": form, "project":project})



@authDecorators.login_required
@http.require_GET
def visitList(request):
    visits = activityModels.SiteVisit.objects.all()
    return render(request, "administration/visits/list.html", {"visits":visits})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST"])
def visitCreate(request):
    if request.POST:
        form = forms.SiteVisitCreateForm(request.POST, request.FILES)
        if form.is_valid():
            visit = form.save()
            if request.FILES['images']:
                for img in request.FILES.getlist('images'):
                    activityModels.SiteVisitImage.objects.create(image=img, site_visit=visit)
            return redirect("administration:visit-list")
        return render(request, "administration/visits/create.html", {"form": form})
    else:
        form = forms.SiteVisitCreateForm()
        return render(request, "administration/visits/create.html", {"form": form})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST", "DELETE"])
def visitUpdateDelete(request, id):
    if request.method == "DELETE":
        activityModels.SiteVisit.objects.get(id=id).delete()
        return HttpResponse(f"SiteVisit {id} deleted")

    visit = activityModels.SiteVisit.objects.prefetch_related('site_visit_images').get(id=id)
    if request.POST:
        form = forms.SiteVisitUpdateForm(instance=visit, data=request.POST, files=request.FILES)
        if form.is_valid():
            visit = form.save()
            if request.FILES['images']:
                for img in request.FILES.getlist('images'):
                    activityModels.SiteVisitImage.objects.create(image=img, site_visit=visit)
            return redirect("administration:visit-update-delete", id=id)
        return render(request, "administration/visits/update.html", {"form": form, "visit":visit})
    form = forms.SiteVisitUpdateForm(instance=visit)
    return render(request, "administration/visits/update.html", {"form": form, "visit":visit}) 

