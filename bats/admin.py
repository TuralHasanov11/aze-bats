from django.contrib import admin

class BatAdmin(admin.ModelAdmin):
    list_display = ("name", "is_red_book",)
    prepopulated_fields = {"slug": ("name",)}  