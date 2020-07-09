from django import forms
from PortApp import models 

class contact(forms.ModelForm):
    class Meta:
        model = models.contact
        fields = ['Username' , 'Email' , 'First_Name' , 'Last_name' , 'Password']