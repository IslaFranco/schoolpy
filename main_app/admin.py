from django.contrib import admin
from .models import Student, Teacher, Assignment, Course

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Assignment)
admin.site.register(Course)
