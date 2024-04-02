# job_applications/urls.py

from django.urls import path
from django.views.generic.base import RedirectView
from .views import apply_for_job, application_accepted, my_job_applications, view_applications_for_employer

app_name = 'job_applications'

urlpatterns = [
    path('', RedirectView.as_view(url='/'), name='redirect_to_home'),
    path('apply/<int:job_posting_id>/', apply_for_job, name='apply_for_job'),
    path('submitted/<int:application_id>/', application_accepted, name='application_accepted'),
    path('my_applications/', my_job_applications, name='my_job_applications'),
    path('employer_applications/', view_applications_for_employer, name='employer_applications'),
]
