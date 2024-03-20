from django.shortcuts import render
from .models import Employee

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})


def view_about(request):   
    return render(request,'about.html',{})


