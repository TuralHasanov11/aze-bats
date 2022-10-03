from django.db import models
from ckeditor import fields as ckeditorFields
from django import urls
from core import helpers


class Family(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Families"

    def __str__(self):
        return self.name


class Genus(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    family = models.ForeignKey(Family, related_name="family", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Genus"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = helpers.generateUUID(self.name)
        return super().save(*args, **kwargs)


class Species(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length = 200, null=True, unique=True)
    cover_image = models.ImageField(upload_to=None)
    description = ckeditorFields.RichTextField(null=True, blank=True)
    distribution = ckeditorFields.RichTextField(null=True, blank=True)
    biology = ckeditorFields.RichTextField(null=True, blank=True)
    conservation = ckeditorFields.RichTextField(null=True, blank=True)
    habitat = ckeditorFields.RichTextField(null=True, blank=True)
    threats = ckeditorFields.RichTextField(null=True, blank=True)
    is_red_book = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Species"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return urls.reverse("bats:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = helpers.generateUUID(self.name)
        return super().save(*args, **kwargs)


class SpeciesImage(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=None)
