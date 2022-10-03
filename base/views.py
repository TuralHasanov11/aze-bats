from django.shortcuts import render

def index(request):
    return render(request, "base/index.html")

def articles(request):
    return render(request, "base/articles.html")