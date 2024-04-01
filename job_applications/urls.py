# job_applications/urls.py

from django.urls import path
from django.views.generic.base import RedirectView
from .views import apply_for_job, application_accepted

app_name = 'job_applications'

urlpatterns = [
    path('', RedirectView.as_view(url='/'), name='redirect_to_home'),
    path('apply/<int:job_posting_id>/', apply_for_job, name='apply_for_job'),
    path('job_applications/submitted/<int:application_id>/', application_accepted, name='application_accepted'),
]
