from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='jobs.index'),
    path('map/', views.map, name='jobs.map'),
    path('<int:id>/', views.show, name='jobs.show'),
    path('<int:id>/apply/', views.apply, name='jobs.apply'),
]