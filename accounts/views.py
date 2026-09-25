from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomErrorList, CustomUserCreationForm, ProfileForm
from .models import Profile

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')
def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            user = form.save()
            role = request.POST.get('role', Profile.SEEKER)
            if role not in (Profile.SEEKER, Profile.RECRUITER):
                role = Profile.SEEKER
            Profile.objects.create(user=user, role=role)
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {'template_data': template_data})

def profile_context(profile, title):
    return {
        'title': title,
        'profile': profile,
        'skills': [s.strip() for s in (profile.skills or '').split(',') if s.strip()],
        'links': [l.strip() for l in (profile.links or '').splitlines() if l.strip()],
    }
@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    template_data = profile_context(profile, 'My Profile')
    template_data['is_own'] = True
    return render(request, 'accounts/profile.html', {'template_data': template_data})

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    template_data = {}
    template_data['title'] = 'Edit Profile'
    if request.method == 'GET':
        template_data['form'] = ProfileForm(instance=profile)
        return render(request, 'accounts/edit_profile.html', {'template_data': template_data})
    elif request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.profile')
        else:
            template_data['form'] = form
            return render(request, 'accounts/edit_profile.html', {'template_data': template_data})

def show_profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    template_data = profile_context(profile, profile.user.username)
    template_data['is_own'] = request.user == profile.user
    return render(request, 'accounts/profile.html', {'template_data': template_data})