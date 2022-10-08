from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teacher/login', views.teacherLogin, name='teacher-login'),
    path('teacher-dashboard/', views.teacherDashboard, name='teacher-dashboard'),
    path('student-dashboard/', views.studentDashboard, name='student-dashboard'),
    path('accounts/signup/student/', views.student_signup, name='student-signup'),
    path('accounts/signup/teacher/', views.teacher_signup, name='teacher-signup'),
]