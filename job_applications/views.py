from django.shortcuts import render
from .forms import JobApplicationForm  # Assuming you have a ModelForm for JobApplication

def apply_for_job(request, job_posting_id):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job_posting_id = job_posting_id
            application.save()
            # Redirect or give feedback that the application was successful
            return redirect('success_page')
    else:
        form = JobApplicationForm()

    return render(request, 'apply_for_job.html', {'form': form})
