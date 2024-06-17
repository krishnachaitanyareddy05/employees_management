from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    employee_id = models.CharField(max_length=20)
    posting_location = models.CharField(max_length=100)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
