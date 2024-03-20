from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Manager(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Salary(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.amount)

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    hiring_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
