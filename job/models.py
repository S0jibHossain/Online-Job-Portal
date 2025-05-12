from django.db import models
from django.contrib.auth import get_user_model
from company.models import Company

User = get_user_model()


class Job(models.Model):
    user = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True)  # NEW FIELD

    title = models.CharField(max_length=100)
    date_time_posted = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(auto_now=True)
    pay = models.PositiveIntegerField()
    pay_mode = models.CharField(
        max_length=30,
        choices=[
            ('Daily', 'Daily'),
            ('Weekly', 'Weekly'),
            ('Monthly', 'Monthly')
        ]
    )
    job_type = models.CharField(
        max_length=30,
        choices=[
            ('Full Time', 'Full Time'),
            ('Part Time', 'Part Time')
        ]
    )
    job_location = models.CharField(
        max_length=30,
        choices=[
            ('Remote', 'Remote'),
            ('Hybrid', 'Hybrid'),
            ('Onsite', 'Onsite')
        ]
    )
    job_cat = models.CharField(
        max_length=20,
        choices=[
            ('Permanent', 'Permanent'),
            ('Contract', 'Contract')
        ]
    )
    expiry_date = models.DateField(null=True)
    house_per_week = models.PositiveIntegerField()
    job_description = models.TextField()

    def save(self, *args, **kwargs):
        if self.user:
            self.company_name = self.user.name  # assumes Company has `name` field
        super().save(*args, **kwargs)


class JobRes(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)


class JobExp(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default="Pending", max_length=50)

