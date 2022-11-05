from django.db import models
from administration import models as administration_models
from core import helpers


class Project(models.Model):
    name = administration_models.NameField()
    slug = administration_models.SlugField()
    cover_image = administration_models.ImageField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = helpers.generateSlug(self.name)
        return super().save(*args, **kwargs)


class SiteVisit(models.Model):
    name = administration_models.NameField()
    slug = administration_models.SlugField()
    cover_image = administration_models.ImageField()

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
    image = administration_models.ImageField()

    def __str__(self) -> str:
        return str(self.project)


class SiteVisitImage(models.Model):
    site_visit = models.ForeignKey(SiteVisit, on_delete=models.CASCADE, related_name="site_visit_images")
    image = administration_models.ImageField()

    def __str__(self) -> str:
        return str(self.site_visit)


class ProjectAttributes(models.Model):
    project = models.ForeignKey(Project, related_name="project_attributes", on_delete=models.CASCADE)
    description = administration_models.RichTextEditorField()
    language = administration_models.LanguageField()

    def __str__(self):
        return str(self.project)


class SiteVisitAttributes(models.Model):
    site_visit = models.ForeignKey(SiteVisit, related_name="site_visit_attributes", on_delete=models.CASCADE)
    description = administration_models.RichTextEditorField()
    results = administration_models.RichTextEditorField()
    language = administration_models.LanguageField()

    def __str__(self):
        return str(self.site_visit)

