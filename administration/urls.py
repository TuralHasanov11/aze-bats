from django.urls import path
from administration import views

app_name='administration'

urlpatterns = [
    path('/', views.index, name="index"),
]
