from django.contrib import admin
from django.contrib.admin import models

from .models import Student, Subject, Grade

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)

