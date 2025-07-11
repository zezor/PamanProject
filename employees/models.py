from django.db import models

# Create your models here.
class Employees(models.Model):
    sur_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    other_name= models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    staff_id = models.CharField(max_length=10)