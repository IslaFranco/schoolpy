from ast import Assign
from operator import imod
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        TEACHER = "TEACHER", 'Teacher'
        STUDENT = "STUDENT", 'Student'

    base_role = Role.ADMIN

    role = models.CharField(max_length=100, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    sex = models.CharField(max_length=10)
    address = models.CharField(max_length=255)


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)


class Student(User):

    base_role = User.Role.STUDENT
    student = StudentManager()
    grade = models.CharField(max_length=100)
    dob = models.DateField()

    class Meta:
        verbose_name_plural = 'Student'
        app_label = 'auth'


class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)


class Teacher(User):

    base_role = User.Role.TEACHER
    teacher = TeacherManager()

    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Teacher'
        app_label = 'auth'


class Course(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    title = models.CharField(max_length=100)
    start_time = models.DateField()
    end_time = models.DateField()
    level = models.CharField(max_length=100)
    course_units = models.IntegerField()
    term = models.CharField(max_length=100)

    teachers = models.ManyToManyField(
        Teacher, through='CourseTaught', related_name='courses')

    students = models.ManyToManyField(
        Student, through='CourseTaken', related_name='courses')

    def __str__(self):
        return f'{self.subject}, {self.title}'

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'course_id': self.id})


class Assignment(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    submitted = models.BooleanField()

    teachers = models.ManyToManyField(
        Teacher, through='TeacherAssignment', related_name='assignment')

    students = models.ManyToManyField(
        Student, through='StudentAssignment', related_name='assignment')

    courses = models.ManyToManyField(
        Student, through='CourseAssignment', related_name='assignment')

    def __str__(self):
        return f'{self.subject}, {self.title}'

    def get_absolute_url(self):
        return reverse('assignment_detail', kwargs={'assignment_id': self.id})


class CourseTaught(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"Teacher: {self.teacher.last_name}, {self.teacher.first_name} - {self.course.title}"


class CourseTaken(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"Student: {self.student.last_name}, {self.student.first_name} - {self.course.title}"


class TeacherAssignment(models.Models):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)


class StudentAssignment(models.Models):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)


class CourseAssignment(models.Models):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
