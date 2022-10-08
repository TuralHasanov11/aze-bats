from email.policy import default
from django.db import models
from ckeditor_uploader import fields as ckeditorFields
from core import helpers
from django.db.models import signals
from django.dispatch import receiver
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
    cover_image = models.ImageField(upload_to=helpers.uploadImageLocation)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = helpers.generateSlug(self.name)
        return super().save(*args, **kwargs)


class SiteVisit(models.Model):
    name = models.CharField(max_length=199, null=False, blank=False)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
    cover_image = models.ImageField(upload_to=helpers.uploadImageLocation)

    class Meta:
        verbose_name = "Site Visit"
        verbose_name_plural = "Site Visits"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = helpers.generateSlug(self.name)
        return super().save(*args, **kwargs)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_images")
    image = models.ImageField(upload_to=helpers.uploadImageLocation)

    def __str__(self) -> str:
        return str(self.project)


class SiteVisitImage(models.Model):
    site_visit = models.ForeignKey(SiteVisit, on_delete=models.CASCADE, related_name="site_visit_images")
    image = models.ImageField(upload_to=helpers.uploadImageLocation)

    def __str__(self) -> str:
        return str(self.site_visit)


class ProjectAttributes(models.Model):
    project = models.ForeignKey(Project, related_name="project_attributes", on_delete=models.CASCADE)
    description = ckeditorFields.RichTextUploadingField(null=True, blank=True)
    language = models.CharField(max_length=2, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)

    def __str__(self):
        return str(self.project)


class SiteVisitAttributes(models.Model):
    site_visit = models.ForeignKey(SiteVisit, related_name="site_visit_attributes", on_delete=models.CASCADE)
    description = ckeditorFields.RichTextUploadingField(null=True, blank=True)
    results = ckeditorFields.RichTextUploadingField(null=True, blank=True)
    language = models.CharField(max_length=2, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)

    def __str__(self):
        return str(self.site_visit)


@receiver(signals.post_delete, sender=Project)
def postProjectDelete(sender, instance, **kwargs):
    instance.cover_image.delete(False)


@receiver(signals.post_delete, sender=SiteVisit)
def postSiteVisitDelete(sender, instance, **kwargs):
    instance.cover_image.delete(False)
