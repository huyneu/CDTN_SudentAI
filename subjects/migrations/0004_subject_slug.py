# Generated by Django 4.0.5 on 2023-01-31 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_subject_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
