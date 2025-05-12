from django.urls import path
from .views import *

urlpatterns = [
    path('add_resume/', add_resume, name='add_resume'),
    path('update_resume/<int:pk>/', update_resume, name='update_resume'),
    path('resume_details/<int:pk>/', resume_details, name='resume_details'),

    path('add_education/<int:pk>/', add_education, name='add_education'),
    path('update_education/<int:pk>/', update_education, name='update_education'),
    path('delete_education/<int:pk>/', delete_education, name='delete_education'),

    path('add_work/<int:pk>/', add_work, name='add_work'),
    path('update_work/<int:pk>/', update_work, name='update_work'),
    path('delete_work/<int:pk>/', delete_work, name='delete_work'),

]
