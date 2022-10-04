from django.contrib import admin
from base import models

@admin.register(models.Author)
class AuthorModel(admin.ModelAdmin):
    pass

@admin.register(models.Article)
class ArticleModel(admin.ModelAdmin):
    pass