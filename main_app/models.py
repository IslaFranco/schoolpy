from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from main_app.views import assignments_detail


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
    description = models.TextField(max_length=255)
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    submitted = models.BooleanField()

    def __str__(self):
        return f'{self.subject}, {self.title}'

    def get_absolute_url(self):
        return reverse('assignment_detail', kwargs={'pk': self.id})


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)


class Student(User):

    base_role = User.Role.STUDENT
    student = StudentManager()
    grade = models.CharField(max_length=100)
    dob = models.DateField()

    teachers = models.ManyToManyField(Teacher)
    courses = models.ManyToManyField(Course)
    assignments = models.ManyToManyField(Assignment)

    class Meta:
        verbose_name_plural = 'Student'
        app_label = 'auth'

    def __str__(self):
        return f'{self.last_name}, {self.first_name} - Grade: {self.grade}'

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.id})


# @receiver(post_save, sender=Student)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and instance.role == "STUDENT":
#         StudentProfile.objects.create(user=instance)


# class StudentProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)


class Teacher(User):

    base_role = User.Role.TEACHER
    teacher = TeacherManager()

    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    students = models.ManyToManyField(Student)
    courses = models.ManyToManyField(Course)
    assignments = models.ManyToManyField(Assignment)

    class Meta:
        verbose_name_plural = 'Teacher'
        app_label = 'auth'

    def __str__(self):
        return f'{self.last_name}, {self.first_name} - Grade: {self.grade}'

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.id})


class Course(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    title = models.CharField(max_length=100)
    start_time = models.DateField()
    end_time = models.DateField()
    level = models.CharField(max_length=100)
    course_units = models.IntegerField()
    term = models.CharField(max_length=100)

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject}, {self.title}'

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.id})
