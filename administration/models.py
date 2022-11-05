from ckeditor_uploader import fields as ckeditorFields
from django.db import models
from django.conf import settings
from core import helpers


class RichTextEditorField(ckeditorFields.RichTextUploadingField):
    description = "Rich text editor field"

    def __init__(self, *args, **kwargs):
        kwargs['null'] = True
        kwargs['blank'] = True
        super().__init__(*args, **kwargs)


class LanguageField(models.CharField):
    description = "Language field"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 2
        kwargs['choices'] = settings.LANGUAGES
        kwargs['default'] = settings.LANGUAGE_CODE
        super().__init__(*args, **kwargs)


class ImageField(models.ImageField):
    description = "Image field"

    def __init__(self, *args, **kwargs):
        kwargs['upload_to'] = helpers.uploadImageLocation
        super().__init__(*args, **kwargs)


class SlugField(models.SlugField):
    description = "Slug field"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255
        kwargs['null'] = True
        kwargs['blank'] = True
        kwargs['unique'] = True
        super().__init__(*args, **kwargs)


class NameField(models.CharField):
    description = "Name field"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 200
        kwargs['null'] = False
        kwargs['blank'] = False
        super().__init__(*args, **kwargs)