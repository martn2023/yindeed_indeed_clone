# job_catalog/urls.py, BORROWING THIS PLACEHOLDER TEXT FROM CHATGPT

from django.urls import path
from . import views

app_name = 'job_catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_companies/', views.display_all_companies, name='all_companies'),
]
