from django.urls import path
from .views import *


urlpatterns = [
    path('register_candidate/', register_candidate, name='register_candidate'),
    path('register_recruiter/', register_recruiter, name='register_recruiter'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('change_password/<int:pk>/', change_password, name='change_password'),
    path('update_profile/<int:pk>/', update_profile, name='update_profile'),

]