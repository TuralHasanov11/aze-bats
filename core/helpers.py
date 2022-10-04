from django.template.defaultfilters import slugify
import uuid


def generateSlug(value):
    return slugify(value) + f"{uuid.uuid4()}"


def uploadBatCoverImageLocation(instance, filename, **kwargs):
    filePath = f'bats/{str(instance.name)}-{uuid.uuid4()}-{filename}'
    return filePath

def uploadAuthorCoverImageLocation(instance, filename, **kwargs):
    filePath = f'authors/{str(instance.name)}-{uuid.uuid4()}-{filename}'
    return filePath


def uploadBatImageLocation(instance, filename, **kwargs):
    filePath = f'bats/{str(instance.species.name)}-{uuid.uuid4()}-{filename}'
    return filePath