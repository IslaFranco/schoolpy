from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Roles(models.TextChoices):
        TEACHER = "TEACHER", 'Teacher'
        STUDENT = "STUDENT", 'Student'

    role = models.CharField(max_length=255, choices=Roles.choices)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    sex = models.CharField(max_length=1)
    address = models.CharField(max_length=255)


class Assignment(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    submitted = models.BooleanField()


class Course(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    title = models.CharField(max_length=100)
    start_time = models.DateField()
    end_time = models.DateField()
    level = models.CharField(max_length=100)
    course_units = models.IntegerField()
    term = models.CharField(max_length=100)
