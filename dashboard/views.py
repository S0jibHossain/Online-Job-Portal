from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from job.models import Job, JobApplication
from company.models import Company
from resume.models import Resume

# Inside the candidate block




def dashboard(request):
    user = request.user
    if hasattr(user, 'is_recruiter') and user.is_recruiter:
        company = Company.objects.filter(user=user).first()

        # Ensure the user's 'has_company' flag is updated
        if company:
            user.has_company = True
            user.save()

        jobs_posted = Job.objects.filter(user=company).count() if company else 0
        applications_received = JobApplication.objects.filter(job__user=company).count() if company else 0

        context = {
            'recruiter_name': user.get_full_name() or user.username,
            'company_name': company.name if company else 'Your Company',
            'profile_image_url': user.profile.image.url if hasattr(user, 'profile') and hasattr(user.profile, 'image') and user.profile.image else '',
            'jobs_posted': jobs_posted,
            'applications_received': applications_received,
            'company_rating': getattr(company, 'rating', 4.5),  # Placeholder if rating isn't in model
            'recent_activity': [
                'You posted a new job: Frontend Developer',
                'You received 5 new applications',
                'Your company profile was updated',
            ],
            'has_company': user.has_company,  # Use the value from the User model
        }
        return render(request, 'dashboard/recruiter_dashboard.html', context)
    elif hasattr(user, 'is_candidate') and user.is_candidate:
        jobs_applied_count = JobApplication.objects.filter(user=user).count()
        interviews_count = JobApplication.objects.filter(user=user, status='Interview').count()
        resume = Resume.objects.filter(user=user).first()

        # Placeholder profile completion (custom logic can replace this)
        profile_completion = 80
        if hasattr(user, 'profile'):
            profile_completion = getattr(user.profile, 'completion_percent', 80)

        context = {
            'candidate_name': user.get_full_name() or user.username,
            'profile_image_url': user.profile.image.url if hasattr(user, 'profile') and hasattr(user.profile,
                                                                                                'image') and user.profile.image else '',
            'candidate_role': 'Job Seeker',
            'jobs_applied_count': jobs_applied_count,
            'interviews_count': interviews_count,
            'profile_completion': profile_completion,
            'suggestions': [
                'Update your resume for better job matches',
                'Check out new jobs in your field',
                'Complete your profile to attract recruiters',
            ],
            'resume': resume  # 👈 This is the key line
        }
        return render(request, 'dashboard/candidate_dashboard.html', context)

    else:
        return render(request, 'dashboard/candidate_dashboard.html')  # fallback
