from django.urls import path
from teacher import views

app_name = "teacher"

urlpatterns = [
    path("", views.teacher_list, name="list"),
    path("<int:id>/", views.teacher_detail, name="detail"),
]
