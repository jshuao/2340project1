from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255, blank=True)
    skills= models.CharField(max_length=255, blank=True, help_text='Seperate skills w/ comma')
    education = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    links = models.TextField(blank=True, help_text='One link per line')

    def skill_list(self):
        return [s.strip() for s in self.skills.split(',') if s.strip()]

    def link_list(self):
        return [l.strip() for l in self.links.splitlines() if l.strip()]

    def __str__(self):
        return self.user.username
