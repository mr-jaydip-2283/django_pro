from datetime import datetime
from django.db import models, connection
from django.utils import timezone

class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Employees(models.Model):
    code = models.CharField(max_length=100, blank=True) 
    firstname = models.TextField() 
    middlename = models.TextField(blank=True, null=True) 
    lastname = models.TextField() 
    gender = models.TextField(blank=True, null=True) 
    dob = models.DateField(blank=True, null=True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.TextField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.firstname} {self.middlename or ''} {self.lastname}".strip()

    def save(self, *args, **kwargs):
        # Automatically set code if blank
        if not self.code:
            self.code = f"EMP{self.pk or Employees.objects.count() + 1}"
        super().save(*args, **kwargs)


# Function to delete all records and reset auto-increment ID in Employees table
def reset_employees_table():
    # Delete all records from Employees table
    Employees.objects.all().delete()
    
    # Reset auto-increment ID to 1
    with connection.cursor() as cursor:
        cursor.execute("ALTER TABLE employee_information_employees AUTO_INCREMENT = 1;")
