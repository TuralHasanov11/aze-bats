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
            form.save()
            return redirect("administration:bat-list")
        return render(request, "administration/bats/create.html", {"form": form})
    else:
        form = forms.CreateBatSpeciesForm()
        return render(request, "administration/bats/create.html", {"form": form})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST"])
def batUpdate(request, id):
    bat = get_object_or_404(batModels.Species, id=id)
    if request.POST:
        form = forms.UpdateBatSpeciesForm(instance=bat, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("administration:bat-update", id=id)
        return render(request, "administration/bats/update.html", {"form": form})
    form = forms.UpdateBatSpeciesForm(instance=bat)
    return render(request, "administration/bats/update.html", {"form": form, "bat":bat})


@authDecorators.login_required
@http.require_POST
def batDelete(request, id):
    batModels.Species.objects.get(id=id).delete()
    return redirect("administration:bat-list")


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
@http.require_http_methods(["GET", "POST"])
def authorUpdateDelete(request, id):
    author = get_object_or_404(baseModels.Author, id=id)
    if request.POST:
        form = forms.UpdateAuthorForm(instance=author, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("administration:author-update-delete", id=id)
        return render(request, "administration/authors/update.html", {"form": form})
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
    articles = baseModels.article.objects.all()
    return render(request, "administration/articles/list.html", {"form": form, "articles":articles})


@authDecorators.login_required
@http.require_http_methods(["GET", "POST"])
def articleUpdateDelete(request, id):
    article = get_object_or_404(baseModels.Article, id=id)
    if request.POST:
        form = forms.ArticleForm(instance=article, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("administration:article-update-delete", id=id)
        return render(request, "administration/articles/update.html", {"form": form})
    form = forms.ArticleForm(instance=article)
    return render(request, "administration/articles/update.html", {"form": form, "article":article})


def projectUpdateDelete(request):
    return render(request, "administration/project_update.html")

def visitListCreate(request):
    return render(request, "administration/visit_list.html")

def visitUpdateDelete(request):
    return render(request, "administration/visit_update.html")

def projectListCreate(request):
    return render(request, "administration/authors/list.html")

