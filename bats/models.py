from django.db import models
from ckeditor_uploader import fields as ckeditorFields
from django import urls
from core import helpers
from django.db.models import signals
from django.dispatch import receiver


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
            self.slug = helpers.generateSlug(self.name)
        return super().save(*args, **kwargs)


class Species(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length = 200, blank=True, unique=True, null=True)
    cover_image = models.ImageField(upload_to=helpers.uploadImageLocation)
    genus = models.ForeignKey(Genus, related_name="genus", on_delete=models.CASCADE)
    description = ckeditorFields.RichTextUploadingField(null=True, blank=True)
    distribution = ckeditorFields.RichTextUploadingField(null=True, blank=True)
    biology = ckeditorFields.RichTextUploadingField(null=True, blank=True)
    conservation = ckeditorFields.RichTextUploadingField(null=True, blank=True)
    habitat = ckeditorFields.RichTextUploadingField(null=True, blank=True)
    threats = ckeditorFields.RichTextUploadingField(null=True, blank=True)
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
            self.slug = helpers.generateSlug(self.name)
        return super().save(*args, **kwargs)


class SpeciesImage(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name="species_images")
    image = models.ImageField(upload_to=helpers.uploadImageLocation)

    def __str__(self):
        return str(self.species)
    


@receiver(signals.post_delete, sender=Species)
def postSpeciesDelete(sender, instance, **kwargs):
    instance.cover_image.delete(False)