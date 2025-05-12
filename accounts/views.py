from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import *

User = get_user_model()

def register_candidate(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_candidate = True
            var.username = var.email
            var.save()
            messages.success(request, 'Account created successfully!, please login.')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong, please try again!')
            context = {'form': form}
            return render(request, 'accounts/register_candidate.html', context)
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'accounts/register_candidate.html', context)


def register_recruiter(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            messages.success(request, 'Account created successfully!, please login.')
            return redirect('login')
        else:
            messages.warning(request, "Something went wrong, please try again!")
            context = {'form': form}
            return render(request, 'accounts/register_recruiter.html', context)
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'accounts/register_recruiter.html', context)


def login_user(request):
    next = ''

    if request.GET:
        next = request.GET['next']

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if next == '':
                return redirect('dashboard')
            else:
                return redirect(next)
        else:
            messages.warning(request, 'Something went wrong, please try again!')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,'You are successfully logged out.')
    return redirect('login')

def change_password(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong, please try again!')
    else:
        form = UserPasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

def update_profile(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateProfileForm(request.user, request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile successfully updated!')
            return redirect(reverse('update_profile', args=[user.pk]))
        else:
            messages.warning(request, 'Something went wrong, please try again!')
            return redirect(reverse('update_profile', args=[user.pk]))

    else:
        form = UpdateProfileForm(instance=user)
        context = {'form': form}
    return render(request, 'accounts/update_profile.html', context)
