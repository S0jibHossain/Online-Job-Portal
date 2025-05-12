from django.urls import path
from .views import *

urlpatterns = [
    path('add_company/', add_company, name='add_company'),
    path('update_company/<int:pk>/', update_company, name='update_company'),
    path('company_details/<int:pk>/', company_details, name='company_details'),

]