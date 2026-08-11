from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("hello/", views.HelloAPI.as_view(), name="hello"),

    path("students/", views.StudentListAPI.as_view(), name="student-list"),
    path("students/<int:id>/", views.StudentDetailAPI.as_view(), name="student-detail"),

    path("classes/", views.ClassListAPI.as_view(), name="class-list"),
    path("classes/<int:id>/", views.ClassDetailAPI.as_view(), name="class-detail"),

    path("teachers/", views.TeacherListAPI.as_view(), name="teacher-list"),
    path("teachers/<int:id>/", views.TeacherDetailAPI.as_view(), name="teacher-detail"),
]