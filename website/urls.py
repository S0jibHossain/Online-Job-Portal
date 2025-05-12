from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('about_us/', about_us, name='about_us'),
    path('contact/', contact, name='contact')
]