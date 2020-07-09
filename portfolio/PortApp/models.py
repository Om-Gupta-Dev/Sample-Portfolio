from django.db import models
from django import forms

# Create your models here.

class contact(models.Model):
    First_Name = models.CharField(max_length=15 )
    Last_name = models.CharField(max_length=15 )
    Username = models.CharField(max_length=30 )
    Email = models.EmailField()
    Password = models.CharField(max_length=30 ) 
    rPassword = models.CharField(max_length=30 )
    
    def __str__(self):
        return self.Username
    