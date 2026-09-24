from django.shortcuts import render

from jobs.views import jobs


def login(request):
    template_data = {}
    template_data['title'] = 'Log in'
    return render(request, 'accounts/login.html', {'template_data': template_data})


def signup(request):
    template_data = {}
    template_data['title'] = 'Sign up'
    return render(request, 'accounts/signup.html', {'template_data': template_data})


def profile(request):
    template_data = {}
    template_data['title'] = 'Profile'
    template_data['jobs'] = jobs[:3]
    return render(request, 'accounts/profile.html', {'template_data': template_data})