# Generated by Django 5.2 on 2025-05-06 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
