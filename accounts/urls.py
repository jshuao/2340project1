from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='accounts.login'),
    path('logput/', views.logout, name='accounts.logout'),
    path('signup/', views.signup, name='accounts.signup'),
    path('profile/', views.profile, name='accounts.profile'),
    path('profile/edit/', views.edit_profile, name='accounts.edit_profile'),
    path('profile/<int:id>/', views.show_profile, name='accounts.show_profile'),
]