from django.urls import path
from students import views

app_name = "students"

urlpatterns = [
    path("", views.home, name="home"),
    path("students/", views.student_list, name="list"),
    path("students/<int:id>/", views.student_detail, name="detail"),
    path('contact/', views.contact, name='contact'),
    path('students/add/', views.student_add, name='add'),
    path('students/<int:id>/edit/', views.student_edit, name='edit'),
    path('signup/', views.signup, name='signup'),
]
