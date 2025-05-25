

# Create your models here.
from django.db import models
from employees.models import Employee

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - Rating: {self.rating}"
