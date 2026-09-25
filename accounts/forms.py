from django import forms
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe

from .models import Profile

from django.contrib.auth.forms import UserCreationForm

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['headline', 'skills', 'education', 'experience', 'links']
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Backend engineer · Atlanta, GA'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python, Django, Postgres'}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'links': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'https://github.com/username'}),
        }
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1',
        'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )
