from django.shortcuts import render

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
    return render(request , 'PortApp/contact.html')
