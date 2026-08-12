from django.urls import path
from . import views_generic

app_name = "api"

urlpatterns = [
    path("hello/", views_generic.HelloAPI.as_view(), name="hello"),

    path("students/", views_generic.StudentListAPI.as_view(), name="student-list"),
    path("students/<int:id>/", views_generic.StudentDetailAPI.as_view(), name="student-detail"),

    path("classes/", views_generic.ClassListAPI.as_view(), name="class-list"),
    path("classes/<int:id>/", views_generic.ClassDetailAPI.as_view(), name="class-detail"),

    path("teachers/", views_generic.TeacherListAPI.as_view(), name="teacher-list"),
    path("teachers/<int:id>/", views_generic.TeacherDetailAPI.as_view(), name="teacher-detail"),
]