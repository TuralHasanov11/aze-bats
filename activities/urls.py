from django.urls import path
from activities import views

app_name='activities'

urlpatterns = [
    path('/projects', views.projects, name="projects"),
    path('/projects/<str:slug>', views.project, name="project"),
    path('/site-visits', views.visits, name="visits"),
    path('/site-visits/<str:slug>', views.visit, name="visit"),
]
