# Generated by Django 5.2 on 2025-04-16 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_time_posted', models.DateTimeField(auto_now_add=True)),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('pay', models.PositiveIntegerField()),
                ('pay_mode', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=30)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=30)),
                ('job_location', models.CharField(choices=[('Remote', 'Remote'), ('Hybrid', 'Hybrid'), ('Onsite', 'Onsite')], max_length=30)),
                ('job_cat', models.CharField(choices=[('Permanent', 'Permanent'), ('Contract', 'Contract')], max_length=20)),
                ('expiry_date', models.DateField(null=True)),
                ('house_per_week', models.PositiveIntegerField()),
                ('job_description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='JobExp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
        ),
        migrations.CreateModel(
            name='JobRes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
        ),
    ]
