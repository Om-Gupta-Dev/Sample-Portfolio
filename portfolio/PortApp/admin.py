from django.contrib import admin
from PortApp import models  as PortModel

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id' , 'Name' , 'Email' , 'Message' ]


# Register your models here.

admin.site.register(PortModel.contact , ContactAdmin)