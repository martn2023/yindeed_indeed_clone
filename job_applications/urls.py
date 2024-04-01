# job_applications/urls.py

from django.urls import path
from django.views.generic.base import RedirectView
from .views import apply_for_job

urlpatterns = [
    path('', RedirectView.as_view(url='/'), name='redirect_to_home'),
    path('apply/<int:job_posting_id>/', apply_for_job, name='apply_for_job'),
]
