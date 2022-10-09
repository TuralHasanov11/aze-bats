from django.urls import path
from base import views

app_name='base'

urlpatterns = [
    path('', views.index, name="index"),
    path('articles', views.articles, name="articles"),
    path('search', views.search, name="search"),
]
