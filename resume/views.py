from django.db.transaction import commit
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

User = get_user_model()

@login_required
def add_resume(request):
    if request.method == 'POST':
        # Check if user already has a resume
        if Resume.objects.filter(user=request.user).exists():
            messages.warning(request, 'You have already created a resume.')
            return redirect(reverse('resume_details', args=[request.user.resume.pk]))

        form = AddResumeForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user

            # Optional: set user.has_resume = True, if used
            # user = User.objects.get(pk=request.user.pk)
            # user.has_resume = True
            var.save()
            # user.save()

            messages.success(request, 'You have just added your resume!')
            return redirect(reverse('resume_details', args=[var.pk]))
        else:
            messages.warning(request, 'Something went wrong! Please try again.')
            return redirect('add_resume')
    else:
        form = AddResumeForm()
        context = {'form': form}
        return render(request, 'resume/add_resume.html', context)

def update_resume(request, pk):
    resume = Resume.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume information has been successfully updated!')
            return redirect(reverse('resume_details', args=[resume.pk]))
        else:
            messages.warning(request, 'Something went wrong! Please try again.')
            return redirect(reverse('resume_details', args=[resume.pk]))
    else:
        form = UpdateResumeForm(instance=resume)
        context = {'form':form}
    return render(request, 'resume/update_resume.html', context)

def resume_details(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    educations = resume.education_set.all()
    works = resume.work_set.all()
    context = {
        'resume': resume,
        'education': educations,
        'work': works
    }
    return render(request, 'resume/resume_details.html', context)

def add_education(request, pk):
    resume = Resume.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddEducationForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.resume = resume
            var.save()
            messages.success(request, 'Education has been successfully added to resume!')
            return redirect(reverse('add_education', args=[resume.pk]))
        else:
            messages.warning(request, 'Something went wrong! Please try again.')
            return redirect(reverse('add_education', args=[resume.pk]))
    else:
        form = AddEducationForm()
        context = {'form':form}
    return render(request, 'resume/add_education.html', context)

def update_education(request, pk):
    education = Education.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateEducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education information has been successfully updated!')
            return redirect(reverse('resume_details', args=[education.resume.pk]))
        else:
            messages.warning(request, 'Something went wrong! Please try again.')
            return redirect(reverse('update_education', args=[education.pk]))
    else:
        form = UpdateEducationForm(instance=education)
        context = {'form':form}
    return render(request, 'resume/update_education.html', context)

def delete_education(request, pk):
    education = Education.objects.get(pk=pk)
    resume = Resume.objects.get(pk=education.resume.pk)
    education.delete()
    messages.success(request, 'Education information has been successfully deleted from your resume')
    return redirect(reverse('resume_details', args=[resume.pk]))

def add_work(request, pk):
    resume = Resume.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddWorkForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.resume = resume
            var.save()
            messages.success(request, 'Work experience has been successfully added to resume!')
            return redirect(reverse('add_work', args=[resume.pk]))
        else:
            messages.warning(request, 'Something went wrong! Please try again.')
            return redirect(reverse('add_work', args=[resume.pk]))
    else:
        form = AddWorkForm()
        context = {'form':form}
    return render(request, 'resume/add_work.html', context)

def update_work(request, pk):
    work = Work.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateWorkForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            messages.success(request, 'Work experiences information has been successfully updated!')
            return redirect(reverse('resume_details', args=[work.resume.pk]))
        else:
            messages.warning(request, 'Something went wrong! Please try again.')
            return redirect(reverse('update_work', args=[work.pk]))
    else:
        form = UpdateWorkForm(instance=work)
        context = {'form':form}
    return render(request, 'resume/update_work.html', context)

def delete_work(request, pk):
    work = Work.objects.get(pk=pk)
    resume = Resume.objects.get(pk=work.resume.pk)
    work.delete()
    messages.success(request, 'Work experiences information has been successfully deleted from your resume')
    return redirect(reverse('resume_details', args=[resume.pk]))



