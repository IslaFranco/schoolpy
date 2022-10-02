from unicodedata import name
from django.shortcuts import render

# Create your views here.
# Add the following import
# from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')  

def index(request):
  return render(request, 'index.html')  

def teacherDashboard(request):
  return render(request, 'teacher-dashboard.html', { 'teachers': teachers })  


class Teacher:
  def __init__(self, first_name, last_name, password, email, phone_num, sex, address, role, subject, description):
    self.first_name = first_name
    self.last_name = last_name
    self.password = password
    self.email = email
    self.phone_num = phone_num
    self.sex = sex
    self.address = address
    self.role = role
    self.subject = subject
    self.description = description


teachers = [
  Teacher('Jane', 'Rudo', 'password', 'j_r@yahoo.com', '123-456-7891', 'F', 'fake-address', 'Teacher', 'Math', 'Difficult'),
]  
print(teachers)
class Student:
  def __init__(self, first_name, last_name, password, email, phone_num, sex, address, role, grade, dob):
    self.first_name = first_name
    self.last_name = last_name
    self.password = password
    self.email = email
    self.phone_num = phone_num
    self.sex = sex
    self.address = address
    self.role = role
    self.grade = grade
    self.dob = dob


students = [
  Student('Jane', 'Rudo', 'password', 'j_r@yahoo.com', '123-456-7891', 'F', 'fake-address', 'Teacher', '10', '2000-02-22'),
]    