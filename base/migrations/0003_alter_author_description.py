# Generated by Django 4.1.1 on 2022-10-05 19:05

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_author_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]