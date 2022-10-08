from django.contrib import admin
from activities import models


class ProjectImageInlineAdmin(admin.StackedInline):
    model= models.ProjectImage

class ProjectAttributesInlineAdmin(admin.StackedInline):
    model= models.ProjectAttributes

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines= [ProjectImageInlineAdmin, ProjectAttributesInlineAdmin]
    list_display= ('name',)
    prepopulated_fields= {'slug': ('name',)}


class SiteVisitImageInlineAdmin(admin.StackedInline):
    model= models.SiteVisitImage

class SiteVisitAttributesInlineAdmin(admin.StackedInline):
    model= models.SiteVisitAttributes


@admin.register(models.SiteVisit)
class SiteVisitAdmin(admin.ModelAdmin):
    inlines= [SiteVisitImageInlineAdmin, SiteVisitAttributesInlineAdmin]
    list_display= ('name',)
    prepopulated_fields= {'slug': ('name',)}