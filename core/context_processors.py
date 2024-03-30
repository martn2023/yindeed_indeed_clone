from django.contrib.auth.models import Group

def global_user_groups(request):
    is_job_poster = False
    if request.user.is_authenticated:
        is_job_poster = request.user.groups.filter(name='JobPosters').exists()
    return {
        'is_job_poster': is_job_poster,
    }
