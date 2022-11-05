from django.template.defaultfilters import slugify
import uuid


def generateSlug(value):
    return slugify(value) + f"{uuid.uuid4()}"


def uploadImageLocation(instance, filename):
    filePath = f'{instance.__class__.__name__}/{str(instance)}-{uuid.uuid4()}-{filename}'
    return filePath
