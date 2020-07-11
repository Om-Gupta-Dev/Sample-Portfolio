from django.shortcuts import render
from django import forms
from django.forms import ValidationError
from PortApp import forms as PortForm

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
    if request.method == "GET":
        form = PortForm.contact()
        return render(request , 'PortApp/contact.html' , {'form':form})

    if request.method == "POST":
        form = PortForm.contact(request.POST)
        if form.is_valid():
            print("\n\n\t Validatin succeed \t Printing User Data......")
            print('' , form.cleaned_data['First_Name'])
            print('' , form.cleaned_data['Last_name'])
            print('' , form.cleaned_data['Username'])
            print('' , form.cleaned_data['Email'])
            print('' , form.cleaned_data['Message'])
            form.save(commit=True)
                    
            return render(request , 'PortApp/thank.html' , {'form':form})
            else:
                raise ValidationError("Both Passwords Should Match..")
        else:
            return render(request , 'PortApp/contact.html' , {'form':form})