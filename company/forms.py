from django import forms
from .models import Company

class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('user', )

class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('user', )