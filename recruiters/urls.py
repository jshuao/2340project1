from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='recruiters.dashboard'),
    path('post/', views.post_job, name='recruiters.post_job'),
    path('candidates/', views.candidates, name='recruiters.candidates'),
    path('review/', views.review, name='recruiters.review'),
]