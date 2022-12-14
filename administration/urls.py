from django.urls import path
from administration import views

app_name='administration'

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('login', views.loginView, name="login"),
    path('logout', views.logoutView, name="logout"),
    path('bats', views.batList, name="bat-list"),
    path('bats/create', views.batCreate, name="bat-create"),
    path('bats/<int:id>', views.batUpdateDelete, name="bat-update-delete"),
    path('projects', views.projectList, name="project-list"),
    path('projects/create', views.projectCreate, name="project-create"),
    path('projects/<int:id>', views.projectUpdateDelete, name="project-update-delete"),
    path('visits', views.visitList, name="visit-list"),
    path('visits/create', views.visitCreate, name="visit-create"),
    path('visits/<int:id>', views.visitUpdateDelete, name="visit-update-delete"),
    path('authors', views.authorListCreate, name="author-list-create"),
    path('authors/<int:id>', views.authorUpdateDelete, name="author-update-delete"),
    path('articles', views.articleListCreate, name="article-list-create"),
    path('articles/<int:id>', views.articleUpdateDelete, name="article-update-delete"),
]
