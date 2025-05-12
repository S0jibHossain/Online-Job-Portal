from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def about_us(request):
    return render(request, 'website/about_us.html')

def contact(request):
    return render(request, 'website/contact.html')