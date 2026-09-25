from django.contrib import admin
from .models import Job, Application

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'city', 'work_mode']
    list_filter = ['work_mode', 'visa_sponsorship']
    search_fields = ['title', 'skills', 'company']

admin.site.register(Job, JobAdmin)
admin.site.register(Application)
