from django.urls import path
from api import views_generic

app_name = "api"
urlpatterns = [
    #students
    path("students/", views_generic.StudentListAPI.as_view(), name="student-list"),
    path("students/<int:pk>/", views_generic.StudentDetailAPI.as_view(), name="student-detail"),

    #teachers
    path("teachers/", views_generic.TeacherListAPI.as_view(), name="teacher-list"),
    path("teachers/<int:pk>/", views_generic.TeacherDetailAPI.as_view(), name="teacher-detail"),

    #classes
    path("classes/", views_generic.ClassListAPI.as_view(), name="class-list"),
    path("classes/<int:pk>/", views_generic.ClassDetailAPI.as_view(), name="class-detail"),
]