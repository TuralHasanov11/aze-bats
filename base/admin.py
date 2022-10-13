from django.contrib import admin
from base import models

class AuthorAttributesInlineAdmin(admin.StackedInline):
    model=models.AuthorAttributes

@admin.register(models.Author)
class AuthorModel(admin.ModelAdmin):
    inlines= (AuthorAttributesInlineAdmin,)

@admin.register(models.Article)
class ArticleModel(admin.ModelAdmin):
    pass
