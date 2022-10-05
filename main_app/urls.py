from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('teacher-dashboard/', views.teacherDashboard, name='teacher-dashboard'),
    path('student-dashboard/', views.studentDashboard, name='student-dashboard'),
    path('accounts/student/signup/', views.student_signup, name='student-signup'),
    path('accounts/teacher/signup/', views.teacher_signup, name='teacher-signup'),

]