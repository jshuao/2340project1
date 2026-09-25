from django.http import Http404
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from .models import Application
from .models import Job

# Placeholder
jobs = [
    {'id': 1, 'title': 'Backend Engineer', 'company': 'Company', 'location': 'Remote', 'salary': '$130K–150K'},
    {'id': 2, 'title': 'Platform Engineer', 'company': 'Company', 'location': 'Atlanta, GA', 'salary': '$115K–130K'},
    {'id': 3, 'title': 'API Developer', 'company': 'Company', 'location': 'Hybrid', 'salary': '$105K–125K'},
    {'id': 4, 'title': 'Data Engineer', 'company': 'Company', 'location': 'Remote', 'salary': '$125K–145K'},
]

def index(request):
    template_data = {}
    template_data['title'] = 'Jobs'
    template_data['jobs'] = Job.objects.order_by('-creation_date')
    return render(request, 'jobs/index.html', {'template_data': template_data})

def show(request, id):
    job = get_object_or_404(Job, id=id)
    template_data = {}
    template_data['title'] = job.title
    template_data['job'] = job
    return render(request, 'jobs/show.html', {'template_data': template_data})

def map(request):
    template_data = {}
    template_data['title'] = 'Job map'
    template_data['jobs'] = jobs
    return render(request, 'jobs/map.html', {'template_data': template_data})

@login_required
def apply(request, id):
    job = get_object_or_404(Job, id=id)
    template_data = {}
    template_data['title'] = 'Apply'
    template_data['job'] = job
    return render(request, 'jobs/apply.html', {'template_data': template_data})