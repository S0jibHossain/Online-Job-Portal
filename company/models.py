from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()

class Company(models.Model):
    user = models.OneToOneField(user_model, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    state = models.CharField(
        max_length=100,
        choices=[
            ('Dhaka', 'Dhaka'),
            ('Rajshahi', 'Rajshahi'),
        ]
    )

    country = models.CharField(
        max_length=100,
        choices=[
            ('Bangladesh', 'Bangladesh'),
        ]
    )
    primary_industry = models.CharField(
        max_length= 100,
        choices=[
            ('Software', 'Software'),
            ('Finance', 'Finance'),
            ('Medicine', 'Medicine'),
            ('Education', 'Education')
        ]
    )
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=255)
    company_size = models.CharField(
        max_length=20,
        choices=[
            ('1 - 15', '1 - 15'),
            ('15 - 40', '15 - 40'),
            ('40 - 70', '40 - 70'),
            ('70 - 200', '70 - 200'),
        ]
    )
    founded_in = models.PositiveIntegerField()
    linkedin = models.URLField()
    twitter = models.URLField()
    website = models.URLField()
    about_company = models.TextField()

