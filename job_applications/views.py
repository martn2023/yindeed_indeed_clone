from django.shortcuts import render, get_object_or_404
from .forms import JobApplicationForm
from .models import JobPosting

def apply_for_job(request, job_posting_id):
    job_posting = get_object_or_404(JobPosting, id=job_posting_id)  # Fetch the JobPosting object
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job_posting = job_posting  # Assign the job_posting directly
            application.save()
            # Redirect or give feedback that the application was successful
            return redirect('success_page')
    else:
        form = JobApplicationForm()

    return render(request, 'job_applications/apply_for_job.html', {'form': form, 'job_posting': job_posting})
