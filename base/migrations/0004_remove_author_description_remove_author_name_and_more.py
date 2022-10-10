# Generated by Django 4.1.1 on 2022-10-10 10:00

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_author_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='description',
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.CreateModel(
            name='AuthorAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('language', models.CharField(choices=[('en', 'English'), ('az', 'Azerbaijani')], default='en', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_attributes', to='base.author')),
            ],
        ),
    ]
