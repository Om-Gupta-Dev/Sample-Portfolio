from django import forms
from PortApp import models 

class contact(forms.ModelForm):
    class Meta:
        model = models.contact
        fields = ['Name' , 'Email' , 'Message' ]
        widgets = {
            'Name':forms.TextInput(attrs={'class':'btn btn-light text-align-centre' , 'id':'field' ,'wrap':"soft" , 'cols':"20"} ),
            'Email':forms.TextInput(attrs={'class':'btn btn-light' , 'id':'field'} ),
            'Message':forms.Textarea(attrs={'class':'btn btn-light' , 'id':'field'} ),
        }