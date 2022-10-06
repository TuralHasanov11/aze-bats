import os
from django import forms
from bats import models as batModels
from base import models as baseModels
from activities import models as activityModels
from ckeditor import widgets as ckeditorWidgets

class CreateBatSpeciesForm(forms.ModelForm):
    is_red_book = forms.ChoiceField(label='Is it a Red Book specie?', widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form__field', 'placeholder':'Name'}))
    genus = forms.ModelChoiceField(label='Genus', initial='Select Genus', widget=forms.Select(attrs={'class':'form-select'}), queryset=batModels.Genus.objects.all())
    description = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    distribution = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    biology = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    conservation = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    habitat = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    threats = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    images = forms.FileField(label="Additional images", widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = batModels.Species
        fields = ['name', 'genus', 'cover_image', 'description', 'distribution', 'biology', 'conservation', 'habitat', 'threats', 'is_red_book']


class UpdateBatSpeciesForm(forms.ModelForm):
    is_red_book = forms.ChoiceField(label='Is it a Red Book specie?', widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form__field', 'placeholder':'Name'}))
    genus = forms.ModelChoiceField(label='Genus', initial='Select Genus', widget=forms.Select(attrs={'class':'form-select'}), queryset=batModels.Genus.objects.all())
    description = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    distribution = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    biology = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    conservation = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    habitat = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    threats = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    images = forms.FileField(label="Additional images", widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)


    class Meta:
        model = batModels.Species
        fields = ['name', 'genus', 'cover_image', 'description', 'distribution', 'biology', 'conservation', 'habitat', 'threats', 'is_red_book']

    def save(self, commit=True):
        post = self.instance
        post.name = self.cleaned_data['name']
        post.description = self.cleaned_data['description']
        post.distribution = self.cleaned_data['distribution']
        post.biology = self.cleaned_data['biology']
        post.conservation = self.cleaned_data['conservation']
        post.habitat = self.cleaned_data['habitat']
        post.threats = self.cleaned_data['threats']
        post.is_red_book = self.cleaned_data['is_red_book']

        if self.cleaned_data['cover_image']:
            post.cover_image = self.cleaned_data['cover_image']

        if commit:
            post.save()
        return post


class CreateAuthorForm(forms.ModelForm):
    description = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())

    class Meta:
        model = baseModels.Author
        fields = ['name', 'description', 'cover_image']

class UpdateAuthorForm(forms.ModelForm):
    description = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())

    class Meta:
        model = baseModels.Author
        fields = ['name', 'description', 'cover_image']
    
    def save(self, commit=True):
        
        post = self.instance
        post.name = self.cleaned_data['name']
        post.description = self.cleaned_data['description']

        if self.cleaned_data['cover_image']:
            post.cover_image = self.cleaned_data['cover_image']

        if commit:
            post.save()
        return post


class ArticleForm(forms.ModelForm):
    class Meta:
        model = baseModels.Author
        fields = '__all__'


class ProjectCreateForm(forms.ModelForm):
    description = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form__field', 'placeholder':'Name'}))
    images = forms.FileField(label="Additional images", widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    
    class Meta:
        model = activityModels.Project
        fields = ['name', 'description', 'cover_image']

class ProjectUpdateForm(forms.ModelForm):
    description = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form__field', 'placeholder':'Name'}))
    images = forms.FileField(label="Additional images", widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = activityModels.Project
        fields = ['name', 'description', 'cover_image']

    def save(self, commit=True):
        project = self.instance
        project.name = self.cleaned_data['name']
        project.description = self.cleaned_data['description']

        if self.cleaned_data['cover_image']:
            project.cover_image = self.cleaned_data['cover_image']

        if commit:
            project.save()
        return project


class SiteVisitCreateForm(forms.ModelForm):
    description = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    results = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    images = forms.FileField(label="Additional images", widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = activityModels.SiteVisit
        fields = ['name', 'description', 'cover_image', 'results']


class SiteVisitUpdateForm(forms.ModelForm):
    description = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    results = forms.CharField(widget=ckeditorWidgets.CKEditorWidget())
    images = forms.FileField(label="Additional images", widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)


    class Meta:
        model = activityModels.SiteVisit
        fields = ['name', 'description', 'cover_image', 'results']
    
    def save(self, commit=True):
        
        post = self.instance
        post.name = self.cleaned_data['name']
        post.description = self.cleaned_data['description']
        post.results = self.cleaned_data['results']

        if self.cleaned_data['cover_image']:
            post.cover_image = self.cleaned_data['cover_image']

        if commit:
            post.save()
        return post