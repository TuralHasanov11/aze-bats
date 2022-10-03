from django.shortcuts import render
from bats import models as batModels
from activities import models as activityModels
from base import models as baseModels

def batListCreate(request):
    return render(request, "administration/bat_list.html")

def batUpdateDelete(request):
    return render(request, "administration/bat_update.html")

def projectListCreate(request):
    return render(request, "administration/project_list.html")

def projectUpdateDelete(request):
    return render(request, "administration/project_update.html")

def visitListCreate(request):
    return render(request, "administration/visit_list.html")

def visitUpdateDelete(request):
    return render(request, "administration/visit_update.html")