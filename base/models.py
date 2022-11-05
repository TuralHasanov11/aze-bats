from django.db import models
from administration import models as administration_models


class Article(models.Model):
    name = administration_models.NameField()
    url = models.URLField(blank=True, null=True)
    author = models.CharField(null=False, blank=False, max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    cover_image = administration_models.ImageField()


class AuthorAttributes(models.Model):
    author = models.ForeignKey(Author, related_name="author_attributes", on_delete=models.CASCADE)
    name = administration_models.NameField(unique=True)
    description = administration_models.RichTextEditorField()
    language = administration_models.LanguageField()

    def __str__(self):
        return self.name
