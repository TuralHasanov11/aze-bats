# Generated by Django 4.1.1 on 2022-10-06 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_alter_project_cover_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_images', to='activities.project'),
        ),
    ]
