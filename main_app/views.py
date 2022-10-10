from unicodedata import name
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Student, Teacher


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')


def teacherLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if request.method == 'POST':
        login(request, user)
        return redirect('teacher-dashboard')


def studentLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if request.method == 'POST':
        login(request, user)
        return redirect('student-dashboard')


def teacherDashboard(request):
    students = Student.objects.all()
    return render(request, 'teacher-dashboard.html', {'students': students})


def studentDashboard(request):
    students = Student.objects.filter(username=request.user)
    return render(request, 'student-dashboard.html', {'students': students})


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)

    return render(request, 'students/detail.html', {'student': student})


class SignUpFormTeacher(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name', 'phone_number', 'sex', 'address', 'subject', 'description')


class SignUpFormStudent(UserCreationForm):
    class Meta:
        model = Student
        fields = ('username', 'email', 'password1', 'password2',
                  'first_name', 'last_name', 'phone_number', 'sex', 'address', 'grade', 'dob')


def teacher_signup(request):
    # define tasks for handing POST request
    form = SignUpFormTeacher()
    error_message = ''
    if request.method == 'POST':
        # capture form inputs from the usercreation form
        form = SignUpFormTeacher(request.POST)
        if form.is_valid():
            user = form.save()
        # programmatically log the user in
            login(request, user)
        # redirect the user to the cats index page
            return redirect('teacher-dashboard')
        # if form is invalid show error message
        else:
            error_message = 'Invalid credentials'
    # define tasks for handling GET request
    context = {'form': form, 'error_message': error_message}
    # render a template with an empty form
    return render(request, 'registration/teacher_signup.html', context)


def student_signup(request):
    # define tasks for handing POST request
    form = SignUpFormStudent()
    error_message = ''
    if request.method == 'POST':
        # capture form inputs from the usercreation form
        form = SignUpFormStudent(request.POST)
        # validate the form inputs
        if form.is_valid():
            # save the input values as a new user to the database
            user = form.save()
            # programmatically log the user in
            login(request, user)
            # redirect the user to the cats index page
            return redirect('student-dashboard')
        # if form is invalid show error message
        else:
            error_message = 'Invalid credentials'
    # define tasks for handling GET request
    context = {'form': form, 'error_message': error_message}
    # redner a template with an empty form
    return render(request, 'registration/student_signup.html', context)
