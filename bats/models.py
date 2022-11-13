from django.db import models
from administration import models as administration_models
from django import urls
from core import helpers
from django.conf import settings

class Family(models.Model):
    name = administration_models.NameField(unique=True)
    slug = administration_models.SlugField()

    class Meta:
        verbose_name_plural = "Families"

    def __str__(self):
        return self.name


class Genus(models.Model):
    name = administration_models.NameField(unique=True)
    slug = administration_models.SlugField()
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
    name = administration_models.NameField(unique=True)
    slug = administration_models.SlugField()
    cover_image = administration_models.ImageField()
    genus = models.ForeignKey(Genus, related_name="genus", on_delete=models.CASCADE)
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
    
    @property
    def get_absolute_cover_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.cover_image.url)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = helpers.generateSlug(self.name)
        return super().save(*args, **kwargs)


class SpeciesAttributes(models.Model):
    species = models.ForeignKey(Species, related_name="species_attributes", on_delete=models.CASCADE)
    description = administration_models.RichTextEditorField()
    habitat = administration_models.RichTextEditorField()
    threats = administration_models.RichTextEditorField()
    distribution = administration_models.RichTextEditorField()
    conservation = administration_models.RichTextEditorField()
    biology = administration_models.RichTextEditorField()
    language = administration_models.LanguageField()

    def __str__(self):
        return str(self.species)


class SpeciesImage(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name="species_images")
    image = administration_models.ImageField()

    def __str__(self):
        return str(self.species)
    

class SpeciesRedBook(models.Model):
    language = administration_models.LanguageField()
    species = models.ForeignKey(Species, related_name="species_red_book", on_delete=models.CASCADE)
    description = administration_models.RichTextEditorField()

    def __str__(self):
        return str(self.species)    