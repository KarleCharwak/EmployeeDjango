from django.contrib import admin
from .models import Department, Manager, Salary, Employee

admin.site.register(Department)
admin.site.register(Manager)
admin.site.register(Salary)
admin.site.register(Employee)
