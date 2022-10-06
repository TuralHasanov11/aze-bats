from django.contrib import admin
from bats import models


class SpeciesImageInlineAdmin(admin.TabularInline):
    model= models.SpeciesImage

@admin.register(models.Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ("name", "is_red_book", 'genus', 'created_at')
    prepopulated_fields = {"slug": ("name",)}  
    inlines= [SpeciesImageInlineAdmin]

@admin.register(models.Genus)
class GenusModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  

@admin.register(models.Family)
class FamilyModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  