# Generated by Django 4.0.5 on 2023-04-10 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_students_user'),
        ('user', '0003_infouser_isstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='infouser',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.students'),
        ),
    ]