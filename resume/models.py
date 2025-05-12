from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=100,
        choices=[
            ('Rajshahi', 'Rajshahi'),
            ('Dhaka', 'Dhaka'),
        ]
    )
    country = models.CharField(
        max_length=100,
        choices=[
            ('Bangladesh', 'Bangladesh'),
        ]
    )
    experience = models.CharField(
        max_length=20,
        choices=[
            ('0-2', '0-2'),
            ('3-10', '3-10'),
            ('11-40', '11-40'),
        ]
    )
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=30,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female')
        ]
    )
    language = models.CharField(
        max_length=100,
        choices=[
            ('English', 'English'),
            ('German', 'German'),
            ('French', 'French'),

        ],
        default='English'
    )
    educational_level = models.CharField(
        max_length=100,
        choices=[
            ('None', 'None'),
            ('Bachelors', 'Bachelors'),
            ('Masters', 'Masters'),
        ]
    )
    twitter = models.URLField()
    linkedin = models.URLField()
    about_candidate = models.TextField()

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    degree_type = models.CharField(
        max_length=100,
        choices=[
            ('Bachelors', 'Bachelors'),
            ('Masters', 'Masters'),
            ('PhD', 'PhD')
        ]
    )
    course = models.CharField(max_length=255)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    still_schooling_here = models.CharField(
        max_length=100,
        choices=[
            ('No', 'No'),
            ('Yes', 'Yes')
        ],
        default='No'
    )

class Work(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    course = models.CharField(max_length=255)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    still_working_here = models.CharField(
        max_length=100,
        choices=[
            ('No', 'No'),
            ('Yes', 'Yes')
        ],
        default='No'
    )