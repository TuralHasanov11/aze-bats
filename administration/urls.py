from django.urls import path
from administration import views

app_name='administration'

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('bats', views.batList, name="bat-list"),
    path('bats/create', views.batCreate, name="bat-create"),
    path('bats/<int:id>', views.batUpdate, name="bat-update"),
    path('bats/<int:id>/delete', views.batDelete, name="bat-delete"),
    path('projects', views.projectListCreate, name="project-list-create"),
    path('projects/<int:id>', views.projectUpdateDelete, name="projects_update_delete"),
    path('visits', views.visitListCreate, name="visit-list-create"),
    path('visits/<int:id>', views.visitUpdateDelete, name="visit-update-delete"),
    path('authors', views.authorListCreate, name="author-list-create"),
    path('authors/<int:id>', views.authorUpdateDelete, name="author-update-delete"),
    path('articles', views.articleListCreate, name="article-list-create"),
    path('articles/<int:id>', views.articleUpdateDelete, name="article-update-delete"),
]
