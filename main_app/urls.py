from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teacher/login', views.teacherLogin, name='teacher-login'),
    path('student/login', views.studentLogin, name='student-login'),
    path('teacher-dashboard/', views.teacherDashboard, name='teacher-dashboard'),
    path('student-dashboard/', views.studentDashboard, name='student-dashboard'),
    path('accounts/signup/student/', views.student_signup, name='student-signup'),
    path('accounts/signup/teacher/', views.teacher_signup, name='teacher-signup'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('assignments/', views.assignments_index, name='assignment_index'),
    path('assignments/<int:assignment_id>/',
         views.assignments_detail, name='assignment_detail'),
    path('assignments/create/', views.AssignmentCreate.as_view(),
         name='assignment_create'),
    path('assignments/<int:pk>/update/',
         views.AssignmentUpdate.as_view(), name='assignment_update'),
    path('assignments/<int:pk>/delete/',
         views.AssignmentDelete.as_view(), name='assignment_delete'),
    path('courses/<int:teacher_id>/', views.courses_index, name='course_index'),
    path('courses/<int:course_id>/', views.courses_detail, name='course_detail'),
    path('courses/create/', views.CourseCreate.as_view(), name='course_create'),
    path('courses/<int:pk>/update/',
         views.CourseUpdate.as_view(), name='course_update'),
    path('courses/<int:pk>/delete/',
         views.CourseDelete.as_view(), name='course_delete'),


]
