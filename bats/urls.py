from django.urls import path
from bats import views

app_name='bats'

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:slug>', views.detail, name="detail"),
]
