from django import forms
from bats import models as batModels
from base import models as baseModels
from activities import models as activityModels
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from ckeditor_uploader import widgets as ckeditor_widgets


class LoginForm(forms.Form):
    username = forms.CharField(label=_("Username"), max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Username')}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':_('Password')}))


class BatSpeciesCreateForm(forms.ModelForm):
    is_red_book = forms.BooleanField(label=_('Is it a Red Book specie?'), widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Name')}))
    genus = forms.ModelChoiceField(label=_('Genus'), initial=_('Select Genus'), widget=forms.Select(attrs={'class':'form-select'}), queryset=batModels.Genus.objects.all())
    cover_image = forms.ImageField(label=_("Cover Image"), widget=forms.ClearableFileInput(attrs={'multiple': False, 'class':'form-control'}), required=False)

    class Meta:
        model = batModels.Species
        fields = ['name', 'genus', 'cover_image', 'is_red_book']


class BatSpeciesUpdateForm(forms.ModelForm):
    is_red_book = forms.BooleanField(label=_('Is it a Red Book specie?'), widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Name')}))
    genus = forms.ModelChoiceField(label=_('Genus'), initial=_('Select Genus'), widget=forms.Select(attrs={'class':'form-select'}), queryset=batModels.Genus.objects.all())
    cover_image = forms.ImageField(label=_("Cover Image"), widget=forms.ClearableFileInput(attrs={'multiple': False, 'class':'form-control'}), required=False)

    class Meta:
        model = batModels.Species
        fields = ['name', 'genus', 'cover_image', 'is_red_book']

    def save(self, commit=True):
        post = self.instance
        post.name = self.cleaned_data['name']
        post.is_red_book = self.cleaned_data['is_red_book']
        post.genus = self.cleaned_data['genus']

        if self.cleaned_data['cover_image']:
            post.cover_image = self.cleaned_data['cover_image']

        if commit:
            post.save()
        return post


class SpeciesAttributesForm(forms.ModelForm):
    language =forms.ChoiceField(label=_("Language"), widget=forms.Select(attrs={"class": "form-select"}), choices=settings.LANGUAGES)
    description = forms.CharField(label=_("Description"), widget=ckeditor_widgets.CKEditorUploadingWidget())
    distribution = forms.CharField(label=_("Distribution"), widget=ckeditor_widgets.CKEditorUploadingWidget())
    biology = forms.CharField(label=_("Biology"), widget=ckeditor_widgets.CKEditorUploadingWidget())
    conservation = forms.CharField(label=_("Conservation"), widget=ckeditor_widgets.CKEditorUploadingWidget())
    habitat = forms.CharField(label=_("Habitat"), widget=ckeditor_widgets.CKEditorUploadingWidget())
    threats = forms.CharField(label=_("Threats"), widget=ckeditor_widgets.CKEditorUploadingWidget())


    class Meta:
        model = batModels.SpeciesAttributes
        fields = ("description", "language", "distribution", "biology", "conservation", "habitat", "threats")

class SpeciesImageForm(forms.ModelForm):
    image = forms.ImageField(label=_("Image"), widget=forms.ClearableFileInput(attrs={'multiple': False, 'class':'form-control'}), required=False)

    class Meta:
        model = activityModels.ProjectImage
        fields = ("image",)

SpeciesAttributesFormset = forms.inlineformset_factory(batModels.Species, batModels.SpeciesAttributes, form=SpeciesAttributesForm, max_num=len(settings.LANGUAGES), can_delete=True)
SpeciesImageFormset = forms.inlineformset_factory(batModels.Species, batModels.SpeciesImage, form=SpeciesImageForm, extra=5, max_num=10, can_delete=True)


class AuthorForm(forms.ModelForm):
    cover_image = forms.ImageField(label=_("Cover Image"), widget=forms.ClearableFileInput(attrs={'multiple': False, 'class':'form-control'}), required=False)

    class Meta:
        model = baseModels.Author
        fields = '__all__'

class AuthorAttributesForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Name')}))
    language =forms.ChoiceField(label=_("Language"), widget=forms.Select(attrs={"class": "form-select"}), choices=settings.LANGUAGES)
    description = forms.CharField(label=_("Description"), widget=ckeditor_widgets.CKEditorUploadingWidget())

    class Meta:
        model = baseModels.AuthorAttributes
        fields = ("description", "language", "name")    
        
AuthorAttributesFormset = forms.inlineformset_factory(baseModels.Author, baseModels.AuthorAttributes, form=AuthorAttributesForm, max_num=len(settings.LANGUAGES), can_delete=True)


class ArticleForm(forms.ModelForm):
    name = forms.CharField(label=_("Name"), widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Name')}))
    url = forms.URLField(label=_("Link"), widget=forms.URLInput(attrs={'class':'form-control', 'placeholder':_('Link')}))
    author = forms.CharField(label=_("Author"), widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Author')}))

    class Meta:
        model = baseModels.Author
        fields = '__all__'


class ProjectCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Name')}))
    cover_image = forms.ImageField(label=_("Cover Image"), widget=forms.ClearableFileInput(attrs={'multiple': False, 'class':'form-control'}), required=False)

    class Meta:
        model = activityModels.Project
        fields = ['name', 'cover_image']


class ProjectUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Name')}))
    cover_image = forms.ImageField(label=_("Cover Image"), widget=forms.ClearableFileInput(attrs={'multiple': False, 'class':'form-control'}), required=False)

    class Meta:
        model = activityModels.Project
        fields = ['name', 'cover_image']

    def save(self, commit=True):
        project = self.instance
        project.name = self.cleaned_data['name']

        if self.cleaned_data['cover_image']:
            project.cover_image = self.cleaned_data['cover_image']

        if commit:
            project.save()
        return project


class ProjectAttributesForm(forms.ModelForm):
    language =forms.ChoiceField(label=_("Language"), widget=forms.Select(attrs={"class": "form-select"}), choices=settings.LANGUAGES)
    description = forms.CharField(label=_("Description"), widget=ckeditor_widgets.CKEditorUploadingWidget())

    class Meta:
        model = activityModels.ProjectAttributes
        fields = ("description", "language")

class ProjectImageForm(forms.ModelForm):
    image = forms.ImageField(label=_("Image"), widget=forms.ClearableFileInput(attrs={'multiple': False, 'class':'form-control'}), required=False)

    class Meta:
        model = activityModels.ProjectImage
        fields = ("image",)

ProjectAttributesFormset = forms.inlineformset_factory(activityModels.Project, activityModels.ProjectAttributes, form=ProjectAttributesForm, max_num=len(settings.LANGUAGES), can_delete=True)
ProjectImageFormset = forms.inlineformset_factory(activityModels.Project, activityModels.ProjectImage, form=ProjectImageForm, extra=5, max_num=10, can_delete=True)


class SiteVisitCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Name')}))
    cover_image = forms.ImageField(label=_("Cover Image"), widget=forms.ClearableFileInput(attrs={'multiple': False, 'class':'form-control'}), required=False)
    
    class Meta:
        model = activityModels.SiteVisit
        fields = ['name', 'cover_image']


class SiteVisitUpdateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':_('Name')}))
    cover_image = forms.ImageField(label=_("Cover Image"), widget=forms.ClearableFileInput(attrs={'multiple': False, 'class':'form-control'}), required=False)

    class Meta:
        model = activityModels.SiteVisit
        fields = ['name', 'cover_image']
    
    def save(self, commit=True):
        post = self.instance
        post.name = self.cleaned_data['name']

        if self.cleaned_data['cover_image']:
            post.cover_image = self.cleaned_data['cover_image']

        if commit:
            post.save()
        return post


class SiteVisitAttributesForm(forms.ModelForm):
    language =forms.ChoiceField(label=_("Language"), widget=forms.Select(attrs={"class": "form-select"}), choices=settings.LANGUAGES)
    description = forms.CharField(label=_("Description"), widget=ckeditor_widgets.CKEditorUploadingWidget())
    results = forms.CharField(label=_("Results"), widget=ckeditor_widgets.CKEditorUploadingWidget())

    class Meta:
        model = activityModels.SiteVisitAttributes
        fields = ("description", "language", "results")

class SiteVisitImageForm(forms.ModelForm):
    image = forms.ImageField(label=_("Image"), widget=forms.ClearableFileInput(attrs={'multiple': False, 'class':'form-control'}), required=False)

    class Meta:
        model = activityModels.SiteVisitImage
        fields = ("image",)

SiteVisitAttributesFormset = forms.inlineformset_factory(activityModels.SiteVisit, activityModels.SiteVisitAttributes, form=SiteVisitAttributesForm, max_num=len(settings.LANGUAGES), can_delete=True)
SiteVisitImageFormset = forms.inlineformset_factory(activityModels.SiteVisit, activityModels.SiteVisitImage, form=SiteVisitImageForm, extra=5, max_num=10, can_delete=True)
