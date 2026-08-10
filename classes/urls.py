from django.urls import path
from classes import views

app_name = "classes"

urlpatterns = [
    path("", views.class_list, name="list"),
    path("<int:id>/", views.class_detail, name="detail"),
]
