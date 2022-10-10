from django.db import models
from ckeditor_uploader import fields as ckeditorFields
from django.dispatch import receiver
from django.db.models import signals
from core import helpers
from django.conf import settings

class Article(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    url = models.URLField(blank=True, null=True)
    author = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    cover_image = models.ImageField(upload_to=helpers.uploadImageLocation)


class AuthorAttributes(models.Model):
    author = models.ForeignKey(Author, related_name="author_attributes", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    description = ckeditorFields.RichTextUploadingField(null=True, blank=True)
    language = models.CharField(max_length=2, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)

    def __str__(self):
        return self.name


@receiver(signals.post_delete, sender=Author)
def postAuthorDelete(sender, instance, **kwargs):
    instance.cover_image.delete(False)