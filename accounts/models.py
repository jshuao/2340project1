from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    SEEKER = 'seeker'
    RECRUITER = 'recruiter'
    ROLE_CHOICES = [(SEEKER, 'Job seeker'), (RECRUITER, 'Recruiter')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=SEEKER)
    headline = models.CharField(max_length=255, blank=True)
    skills = models.CharField(max_length=500, blank=True, help_text='Comma seperated')
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    links = models.TextField(blank=True, help_text='One URL per line')

    def __str__(self):
        return f'{self.user.username} ({self.role})'
