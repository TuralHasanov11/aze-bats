from django.urls import path
from administration import views

app_name='administration'

urlpatterns = [
    path('/bats', views.batListCreate, name="bat-list-create"),
    path('/bats/<int:id>', views.batUpdateDelete, name="bat-update-delete"),
    path('/projects', views.projectListCreate, name="project-list-create"),
    path('/projects/<int:id>', views.projectUpdateDelete, name="projects_update_delete"),
    path('/visits', views.visitListCreate, name="visit-list-create"),
    path('/visits/<int:id>', views.visitUpdateDelete, name="visit-update-delete"),
]
