from django import forms
from .models import *

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['user', 'date_time_posted', 'date_posted', 'is_published']

class UpdateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['user', 'date_time_posted', 'date_posted', 'is_published']


class AddJobRes(forms.ModelForm):
    class Meta:
        model = JobRes
        fields = ['name']


class AddJobExp(forms.ModelForm):
    class Meta:
        model = JobRes
        fields = ['name']

