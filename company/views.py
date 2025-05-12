from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddCompanyForm
from .models import Company

def add_company(request):
    if request.method == 'POST':
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()

            # Set has_company to True for the user after creating a company
            request.user.has_company = True
            request.user.save()

            messages.success(request, 'Your Company information has been added and saved successfully!')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong. Please try again!')
            return redirect('add_company')
    else:
        form = AddCompanyForm()
        context = {'form': form}
    return render(request, 'company/add_company.html', context)

def update_company(request, pk):
    company = Company.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateCompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company information has been successfully updated!')
            return redirect(reverse('company_details', args=[company.pk]))
        else:
            messages.warning(request, 'Something went wrong. Please try again!!')
            return redirect(reverse('company_details', args=[company.pk]))
    else:
        form = UpdateCompanyForm(instance=company)
        context = {'form': form}
    return render(request, 'company/update_company.html', context)

def company_details(request, pk):
    company = Company.objects.get(pk=pk)
    context = {'company': company}
    return render(request, 'company/company_details.html', context)




