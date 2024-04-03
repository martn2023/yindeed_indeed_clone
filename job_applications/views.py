from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from collections import defaultdict
from .forms import JobApplicationForm
from .models import JobPosting, JobApplication

def apply_for_job(request, job_posting_id):
    job_posting = get_object_or_404(JobPosting, pk=job_posting_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            existing_application = JobApplication.objects.filter(
                user=request.user,
                job_posting=job_posting
            ).exists()
            if existing_application:
                messages.error(request, "You have already applied for this job.")
                return redirect('job_applications:apply_for_job', job_posting_id=job_posting_id)
            application = form.save(commit=False)
            application.user = request.user
            application.job_posting = job_posting
            application.save()
            return redirect('job_applications:application_accepted', application_id=application.id)
        else:
            context = {
                'form': form,
                'job_posting': job_posting
            }
            return render(request, 'job_applications/apply_for_job.html', context)
    else:
        form = JobApplicationForm(initial={'job_posting': job_posting_id, 'user': request.user.id})
        context = {
            'form': form,
            'job_posting': job_posting
        }
        return render(request, 'job_applications/apply_for_job.html', context)

def application_accepted(request, application_id):
    application = get_object_or_404(JobApplication, pk=application_id)
    return render(request, 'job_applications/application_accepted.html', {'application': application})

def my_job_applications(request):
    if not request.user.is_authenticated:
        return redirect(reverse('core:login_start'))
    job_applications = JobApplication.objects.filter(user=request.user).select_related(
        'job_posting__organization').order_by('-submit_date')
    applications_grouped = defaultdict(list)
    for job_app in job_applications:
        applications_grouped[job_app.job_posting.organization].append(job_app)
    context = {
        'applications_grouped': dict(applications_grouped)
    }
    return render(request, 'job_applications/users_job_applications.html', context)

def view_applications_for_employer(request):
    if not request.user.is_authenticated:
        return redirect('core:login_start')
    if hasattr(request.user, 'profile') and request.user.profile.organization:
        employer_org = request.user.profile.organization
        job_postings = JobPosting.objects.filter(organization=employer_org)
        total_applications_count = 0
        applications_grouped_by_job = defaultdict(list)
        for job_posting in job_postings:
            applications = JobApplication.objects.filter(job_posting=job_posting).select_related('user').order_by('submit_date')
            applications_grouped_by_job[job_posting].extend(applications)
            total_applications_count += applications.count()
        context = {
            'applications_grouped_by_job': dict(applications_grouped_by_job),
            'employer_org': employer_org,
            'total_applications_count': total_applications_count,
        }
        return render(request, 'job_applications/employer_applications.html', context)
    else:
        return render(request, 'job_applications/unauthorized.html')


def employer_application_details(request, application_id):
    if not request.user.is_authenticated:
        return redirect('core:login_start')

    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        # If UserProfile doesn't exist for the user, show unauthorized access page
        return render(request, 'job_applications/unauthorized.html', {
            'message': 'You do not have permission to view this page.'
        })

    application = get_object_or_404(JobApplication, pk=application_id)

    # Ensure the application belongs to a job posting of the employer's organization
    if application.job_posting.organization == user_profile.organization:
        return render(request, 'job_applications/employer_application_detail.html', {'application': application})
    else:
        return render(request, 'job_applications/unauthorized.html', {
            'message': 'You do not have permission to view this application.'
        })