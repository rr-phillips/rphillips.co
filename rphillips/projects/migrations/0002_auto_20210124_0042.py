# Generated by Django 3.1.3 on 2021-01-24 00:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
