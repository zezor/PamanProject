from django.contrib import admin

# Register your models here.
from .models import Employees

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = (
        'sur_name', 'first_name', 'other_name', 'date_of_birth',
        'phone_number', 'email', 'address'
    )
    search_fields = ('sur_name', 'first_name', 'other_name', 'email', 'phone_number')
    list_filter = ('date_of_birth',)