from django.contrib import admin

# Register your models here.
from .models import biodata


class BioData_admin(admin.ModelAdmin):
    list_display = ('name' , 'age' , 'form')

admin.site.register(biodata , BioData_admin)