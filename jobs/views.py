from django.http import Http404
from django.shortcuts import render

# Placeholder
jobs = [
    {'id': 1, 'title': 'Backend Engineer', 'company': 'Company', 'location': 'Remote', 'salary': '$130K–150K'},
    {'id': 2, 'title': 'Platform Engineer', 'company': 'Company', 'location': 'Atlanta, GA', 'salary': '$115K–130K'},
    {'id': 3, 'title': 'API Developer', 'company': 'Company', 'location': 'Hybrid', 'salary': '$105K–125K'},
    {'id': 4, 'title': 'Data Engineer', 'company': 'Company', 'location': 'Remote', 'salary': '$125K–145K'},
]


def get_job(id):
    for job in jobs:
        if job['id'] == id:
            return job
    raise Http404('Job not found')


def index(request):
    template_data = {}
    template_data['title'] = 'Jobs'
    template_data['jobs'] = jobs
    return render(request, 'jobs/index.html', {'template_data': template_data})


def show(request, id):
    job = get_job(id)
    template_data = {}
    template_data['title'] = job['title']
    template_data['job'] = job
    return render(request, 'jobs/show.html', {'template_data': template_data})


def map(request):
    template_data = {}
    template_data['title'] = 'Job map'
    template_data['jobs'] = jobs
    return render(request, 'jobs/map.html', {'template_data': template_data})


def apply(request, id):
    job = get_job(id)
    template_data = {}
    template_data['title'] = 'Apply'
    template_data['job'] = job
    return render(request, 'jobs/apply.html', {'template_data': template_data})