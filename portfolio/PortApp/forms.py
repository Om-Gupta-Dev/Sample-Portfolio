from django import forms
from PortApp import models 

class contact(forms.ModelForm):
    class Meta:
        model = models.contact
        fields = ['First_Name' , 'Last_name' , 'Username' , 'Email' , 'Password']
        widgets = {
            'First_Name':forms.TextInput(attrs={'class':'btn btn-warning' , 'id':'enter'} ),
            'Last_name':forms.TextInput(attrs={'class':'btn btn-warning' , 'id':'enter'} ),
            'Username':forms.TextInput(attrs={'class':'btn btn-warning' , 'id':'enter'} ),
            'Email':forms.TextInput(attrs={'class':'btn btn-warning' , 'id':'enter'} ),
            'Password':forms.TextInput(attrs={'class':'btn btn-warning' , 'id':'enter'} ),
        }