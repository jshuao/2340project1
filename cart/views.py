from django.shortcuts import render

from jobs.models import Job


def index(request):
    template_data = {}
    template_data['title'] = 'Cart'
    template_data['jobs'] = Job.objects.all()
    return render(request, 'cart/index.html', {'template_data': template_data})


def compare(request):
    template_data = {}
    template_data['title'] = 'Compare'
    template_data['jobs'] = Job.objects.all()
    return render(request, 'cart/compare.html', {'template_data': template_data})