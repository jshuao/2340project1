from django.shortcuts import render
from jobs.models import Job

# Create your views here.


def dashboard(request):
    template_data = {}
    template_data['title'] = 'Recruiter dashboard'
    template_data['jobs'] = Job.objects.all()
    return render(request, 'recruiters/dashboard.html', {'template_data': template_data})


def post_job(request):
    template_data = {}
    template_data['title'] = 'Post a job'
    return render(request, 'recruiters/post_job.html', {'template_data': template_data})


def candidates(request):
    template_data = {}
    template_data['title'] = 'Candidates'
    template_data['candidates'] = ['Candidate 1', 'Candidate 2', 'Candidate 3', 'Candidate 4']
    return render(request, 'recruiters/candidates.html', {'template_data': template_data})


def review(request):
    template_data = {}
    template_data['title'] = 'Review applicant'
    return render(request, 'recruiters/review.html', {'template_data': template_data})