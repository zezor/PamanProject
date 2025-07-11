from django.contrib import admin

# Register your models here.
from .models import Employees

class Employees(models.Model):
    sur_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    other_name= models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)