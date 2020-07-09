from django.shortcuts import render
from PortApp import forms

# Create your views here.

def home(request):
    return render(request , 'PortApp/home.html')

def about(request):
    return render(request , 'PortApp/about.html')

def services(request):
    return render(request , 'PortApp/services.html')

def fitness(request):
    return render(request , 'PortApp/fitness.html')

def blog(request):
    return render(request , 'PortApp/blog.html')

def contact(request):
    form = forms.contact
    return render(request , 'PortApp/contact.html' , {'form':form})
