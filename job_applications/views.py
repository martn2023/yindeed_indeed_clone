from django.shortcuts import render, get_object_or_404, redirect
from .forms import JobApplicationForm
from .models import JobPosting, JobApplication

def apply_for_job(request, job_posting_id):
    job_posting = get_object_or_404(JobPosting, pk=job_posting_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job_posting = job_posting
            application.save()
            return redirect('job_applications:application_accepted', application_id=application.id)
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
