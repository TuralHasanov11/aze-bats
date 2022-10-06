from django.contrib import admin
from activities import models


class ProjectImageInlineAdmin(admin.TabularInline):
    model= models.ProjectImage

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines= [ProjectImageInlineAdmin,]
    list_display= ('name',)
    prepopulated_fields= {'slug': ('name',)}


class SiteVisitImageInlineAdmin(admin.TabularInline):
    model= models.SiteVisitImage

@admin.register(models.SiteVisit)
class SiteVisitAdmin(admin.ModelAdmin):
    inlines= [SiteVisitImageInlineAdmin,]
    list_display= ('name',)
    prepopulated_fields= {'slug': ('name',)}