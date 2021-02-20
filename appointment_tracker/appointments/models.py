import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Department(models.Model):
    department_id = models.IntegerField(primary_key=True, unique=True, null=False)
    department_name = models.CharField(max_length=100)


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True, unique=True, null=False)
    employee_firstname = models.CharField(max_length=20)
    employee_lastname = models.CharField(max_length=20)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)


class Appointment(models.Model):
    appointment_id = models.IntegerField(primary_key=True, unique=True, null=False, default="")
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    appointment_text = models.TextField()
    appointment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.appointment_id} - {self.appointment_text} - {self.appointment_date}'

    def was_published_recently(self):
        return self.appointment_date >= timezone.now() - datetime.timedelta(days=1)


class Reply(models.Model):
    reply_id = models.IntegerField(primary_key=True, unique=True, null=False)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reply_text = models.TextField()
    reply_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.reply_id} - {self.reply_text} - {self.reply_date}'

    def was_published(self):
        return self.reply_date >= timezone.now() - datetime.timedelta(days=1)
