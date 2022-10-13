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


class Assignment(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    submitted = models.BooleanField()

    def __str__(self):
        return f'{self.subject}, {self.title}'

    def get_absolute_url(self):
        return reverse('assignment_detail', kwargs={'assignment_id': self.id})


class Course(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    title = models.CharField(max_length=100)
    start_time = models.DateField()
    end_time = models.DateField()
    level = models.CharField(max_length=100)
    course_units = models.IntegerField()
    term = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.subject}, {self.title}'

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'course_id': self.id})


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)


class Student(User):

    base_role = User.Role.STUDENT
    student = StudentManager()
    grade = models.CharField(max_length=100)
    dob = models.DateField()

    models.ManyToManyField(Course)

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

    courses = models.ManyToManyField(Course)
    students = models.ManyToManyField(Student)

    class Meta:
        verbose_name_plural = 'Teacher'
        app_label = 'auth'
