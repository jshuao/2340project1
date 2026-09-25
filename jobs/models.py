from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    WORK_MODES = [
        ('On-site', 'On-site'),
        ('Remote', 'Remote'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.TextField()
    city = models.CharField(max_length=255)
    salary_min = models.IntegerField(default=0)
    salary_max = models.IntegerField()
    work_mode = models.CharField(max_length=255, choices=WORK_MODES, default='On-site')
    visa_sponsorship = models.BooleanField(default=False)
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.title
    
    def skill_list(self):
        return [s.strip() for s in self.skills.split(',') if s.strip()]



class Application(models.Model):
    STATUSES = [
        ('Applied', 'Applied'),
        ('Review', 'Review'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Closed', 'Closed'),
    ]

    id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE) #delete all job object and the User object related to this. 
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    status = models.CharField(max_length=255, choices=STATUSES, default='Applied')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ' - ' + ' → ' + self.job.title