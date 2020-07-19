from django.db import models
from django import forms

# Create your models here.

class contact(models.Model):
    Name = models.CharField(max_length=50 )
    Email = models.EmailField()
    Message = models.TextField() 
    
    def __str__(self):
        return self.Username
    