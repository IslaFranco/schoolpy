from django.db import model
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
