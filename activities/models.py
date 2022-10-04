from django.db import models
from ckeditor import fields as ckeditorFields
from core import helpers

class Project(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    cover_image = models.ImageField(upload_to=None)
    description = ckeditorFields.RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = helpers.generateSlug(self.name)
        return super().save(*args, **kwargs)


class SiteVisit(models.Model):
    name = models.CharField(max_length=199, null=False, blank=False)
    cover_image = models.ImageField(upload_to=None)
    description = ckeditorFields.RichTextField(null=True, blank=True)
    results = ckeditorFields.RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = "Site Visit"
        verbose_name_plural = "Site Visits"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = helpers.generateSlug(self.name)
        return super().save(*args, **kwargs)