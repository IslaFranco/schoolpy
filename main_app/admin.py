from django.contrib import admin
from .models import Student, Teacher, Assignment, Course, CourseTaught, CourseTaken

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(CourseTaught)
admin.site.register(CourseTaken)
admin.site.register(StudentAssignment)
admin.site.register(TeacherAssignment)
admin.site.register(CourseAssignment)
