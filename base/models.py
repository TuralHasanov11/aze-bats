from django.db import models
from ckeditor_uploader import fields as ckeditorFields
from django.dispatch import receiver
from django.db.models import signals
from core import helpers

class Article(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    url = models.URLField(blank=True, null=True)
    author = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    cover_image = models.ImageField(upload_to=helpers.uploadImageLocation)
    description = ckeditorFields.RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.name


@receiver(signals.post_delete, sender=Author)
def postAuthorDelete(sender, instance, **kwargs):
    instance.cover_image.delete(False)