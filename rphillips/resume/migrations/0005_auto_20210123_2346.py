# Generated by Django 3.1.3 on 2021-01-23 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20201124_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='start',
            field=models.DateTimeField(),
        ),
    ]