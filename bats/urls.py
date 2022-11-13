from django.urls import path
from bats import views

app_name='bats'

urlpatterns = [
    path('', views.index, name="index"),
    path('gallery', views.gallery, name="gallery"),
    path('<str:slug>', views.detail, name="detail"),
]
