from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from company.models import Company

User = get_user_model()

@login_required
def create_job(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            company = Company.objects.get(pk=request.user.company.pk)
            var.user = company  # Link to company, ensure 'user' is set
            var.save()
            messages.success(request, 'New Job has been Created successfully!!')
            return redirect('create_job')
        else:
            # Print form errors for debugging
            print(form.errors)
            messages.warning(request, 'Something went wrong, please try again!!')
            return redirect('create_job')
    else:
        form = CreateJobForm()
        context = {'form': form}
    return render(request, 'job/create_job.html', context)
@login_required
def update_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'job information has been successfully updated!')
            return redirect(reverse('job_details', args=[job.pk]))
        else:
            messages.warning(request, 'Something went wrong, please try again!!')
            return redirect(reverse('job_details', args=[job.pk]))
    else:
        form = UpdateJobForm(instance=job)
        context = {'form': form}
    return render(request, 'job/update_job.html', context)

@login_required
def delete_job(request, pk):
    job = Job.objects.get(pk=pk)
    job.delete()
    messages.success(request, 'Job has been successfully deleted!')
    return redirect('job_per_company')

@login_required
def job_per_company(request):
    company = Company.objects.get(pk=request.user.company.pk)
    jobs = company.job_set.all()
    context = {'jobs': jobs}
    return render(request, 'job/jobs_per_company.html', context)

@login_required
def job_details(request, pk):
    job = Job.objects.get(pk=pk)
    context = {'job': job}
    return render(request, 'job/job_details.html', context)

def job_list(request):
    jobs = Job.objects.all()

    title = request.GET.get('title')
    location = request.GET.get('location')
    job_type = request.GET.get('job_type')
    min_salary = request.GET.get('min_salary')
    max_salary = request.GET.get('max_salary')

    if title:
        jobs = jobs.filter(title__icontains=title)
    if location:
        jobs = jobs.filter(job_location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if min_salary:
        jobs = jobs.filter(pay__gte=min_salary)
    if max_salary:
        jobs = jobs.filter(pay__lte=max_salary)

    context = {'jobs': jobs}
    return render(request, 'job/job_list.html', context)

@login_required
def apply_for_job(request, pk):
    job = Job.objects.get(pk=pk)
    JobApplication.objects.get_or_create(user=request.user, job=job)
    messages.success(request, "You have applied for this job.")
    return redirect('job_details', pk=pk)

@login_required
def add_jobres(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddJobRes(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.job = job
            var.save()
            messages.success(request, 'New job has successfully added!')
            return redirect(reverse('add_jobres', args=[job.pk]))
        else:
            messages.warning(request, 'Something went wrong, please try again!')
            return redirect(reverse('add_jobres', args=[job.pk]))
    else:
        form = AddJobRes()
        context = {'form': form}
    return render(request, 'job/add_jobres.html', context)

@login_required
def add_jobexp(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddJobExp(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.job = job
            var.save()
            messages.success(request, 'New job has successfully added!')
            return redirect(reverse('add_jobexp', args=[job.pk]))
        else:
            messages.warning(request, 'Something went wrong, please try again!')
            return redirect(reverse('add_jobexp', args=[job.pk]))
    else:
        form = AddJobExp()
        context = {'form': form}
    return render(request, 'job/add_jobexp.html', context)

@login_required
def delete_jobres(request, pk):
    jobres = JobRes.objects.get(pk=pk)
    get_job = jobres.job
    jobres.delete()
    messages.success(request, 'Job responsibility has been deleted!')
    return redirect(reverse('job_details', args=[get_job.pk]))

@login_required
def delete_jobexp(request, pk):
    jobexp = JobExp.objects.get(pk=pk)
    get_job = jobexp.job
    jobexp.delete()
    messages.success(request, 'Job experience has been deleted!')
    return redirect(reverse('job_details', args=[get_job.pk]))


@login_required
def application_status(request):
    applications = JobApplication.objects.filter(user=request.user).select_related('job')
    context = {'applications': applications}
    return render(request, 'job/application_status.html', context)

@login_required
def view_applications(request):
    try:
        company = Company.objects.get(user=request.user)
    except Company.DoesNotExist:
        messages.warning(request, "You need to create a company profile first.")
        return redirect('add_company')

    jobs = Job.objects.filter(user=company)
    applications = JobApplication.objects.filter(job__in=jobs).select_related('job', 'user')

    title_filter = request.GET.get('title')
    status_filter = request.GET.get('status')

    if title_filter:
        applications = applications.filter(job__title__icontains=title_filter)
    if status_filter:
        applications = applications.filter(status=status_filter)

    context = {
        'applications': applications,
        'title_filter': title_filter or '',
        'status_filter': status_filter or '',
    }
    return render(request, 'job/view_applications.html', context)

@login_required
def accept_application(request, app_id):
    application = JobApplication.objects.get(pk=app_id)

    # Ensure the logged-in user is the recruiter for the job
    if application.job.user != request.user.company:
        messages.warning(request, "You are not authorized to accept/reject this application.")
        return redirect('view_applications')

    # Set the status of the application to 'Shortlisted'
    application.status = 'Shortlisted'
    application.save()

    messages.success(request, f"Application for {application.user.get_full_name()} has been accepted.")
    return redirect('view_applications')


@login_required
def reject_application(request, app_id):
    application = JobApplication.objects.get(pk=app_id)

    # Ensure the logged-in user is the recruiter for the job
    if application.job.user != request.user.company:
        messages.warning(request, "You are not authorized to accept/reject this application.")
        return redirect('view_applications')

    # Set the status of the application to 'Rejected'
    application.status = 'Rejected'
    application.save()

    messages.error(request, f"Application for {application.user.get_full_name()} has been rejected.")
    return redirect('view_applications')
