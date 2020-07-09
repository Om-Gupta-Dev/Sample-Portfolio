from django.db import models
from django import forms

# Create your models here.

class contact(models.Model):
    Username = models.CharField(max_length=30)
    Email = models.EmailField()
    First_Name = models.CharField(max_length=15)
    Last_name = models.CharField(max_length=15)
    Password = models.CharField(max_length=30) 
    
    def __str__(self):
        return self.Username
    