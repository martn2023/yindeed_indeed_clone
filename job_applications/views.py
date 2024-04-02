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
            # Check for an existing application
            existing_application = JobApplication.objects.filter(
                user=request.user,
                job_posting=job_posting
            ).exists()

            if existing_application:
                # User has already applied
                messages.error(request, "You have already applied for this job.")
                return redirect('job_applications:apply_for_job', job_posting_id=job_posting_id)

            application = form.save(commit=False)
            application.user = request.user
            application.job_posting = job_posting
            application.save()
            return redirect('job_applications:application_accepted', application_id=application.id)
        else:
            # Form is not valid, show the form again with errors
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
        # Redirect to login page
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
