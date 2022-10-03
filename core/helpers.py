from django.template.defaultfilters import slugify
import uuid


def generateUUID(value):
    return slugify(value) + f"{uuid.uuid4()}"