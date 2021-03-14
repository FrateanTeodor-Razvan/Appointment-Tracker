from django.contrib import admin
from .models import Appointment, Reply, Department, Employee


# Register your models here.
admin.site.register(Appointment)
admin.site.register(Reply)
admin.site.register(Department)
admin.site.register(Employee)
