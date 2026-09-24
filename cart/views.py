from django.shortcuts import render

from jobs.views import jobs


def index(request):
    template_data = {}
    template_data['title'] = 'Cart'
    template_data['jobs'] = jobs[:3]
    return render(request, 'cart/index.html', {'template_data': template_data})


def compare(request):
    template_data = {}
    template_data['title'] = 'Compare'
    template_data['jobs'] = jobs[:3]
    return render(request, 'cart/compare.html', {'template_data': template_data})