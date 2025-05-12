from django.urls import path
from .views import *

urlpatterns = [
    path('create_job/', create_job, name='create_job'),
    path('update_job/<int:pk>/', update_job, name='update_job'),
    path('delete_job/<int:pk>/', delete_job, name='delete_job'),
    path('jobs_per_company/', job_per_company, name='jobs_per_company'),
    path('job_details/<int:pk>/', job_details, name='job_details'),
    path('all/', job_list, name='job_list'),
    path('add_jobres/<int:pk>/', add_jobres, name='add_jobres'),
    path('add_jobexp/<int:pk>/', add_jobexp, name='add_jobexp'),
    path('delete_jobres/<int:pk>/', delete_jobres, name='delete_jobres'),
    path('delete_jobexp/<int:pk>/', delete_jobexp, name='delete_jobexp'),
    path('apply/<int:pk>/', apply_for_job, name='apply_for_job'),
    path('my-applications/', application_status, name='application_status'),
    path('applications/', view_applications, name='view_applications'),
    path('application/<int:app_id>/accept/', accept_application, name='accept_application'),
    path('application/<int:app_id>/reject/', reject_application, name='reject_application'),
]