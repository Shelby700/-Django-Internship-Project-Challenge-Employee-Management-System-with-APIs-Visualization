from django.core.management.base import BaseCommand
from employees.models import Employee
from departments.models import Department
from attendance.models import Attendance
from performance.models import Performance
from faker import Faker
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        departments = ['HR', 'Engineering', 'Sales', 'Finance']
        dept_objs = [Department.objects.get_or_create(name=name)[0] for name in departments]

        for _ in range(50):
            dept = random.choice(dept_objs)
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(), 
                address=fake.address(),
                date_of_joining=fake.date_this_decade(), 
                department=dept
            )

            Attendance.objects.create(
                employee=emp,
                date=fake.date_this_year(),
                status=random.choice(['Present', 'Absent', 'Late'])
            )

            Performance.objects.create(
                employee=emp,
                rating=random.randint(1, 5),
                review_date=fake.date_this_year()
            )
