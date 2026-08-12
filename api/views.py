from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404
from students.models import Student
from classes.models import Class
from teacher.models import Teacher
from api.serializers import (
    StudentSerializer,
    ClassSerializer,
    TeacherSerializer,
)


# Student
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.select_related("class_name")
    serializer_class = StudentSerializer

    #same override you used in class 9
    def get_queryset(self):
        qs = Student.objects.select_related("class_name")
        class_id = self.request.query_params.get("class_id")
        if class_id:
            qs = qs.filter(class_name_id=class_id)
        return qs

    #add a custom endpoint: /api/students/adults/
    @action(detail=False, methods=["get"])
    def adults(self, request):
        qs = self.get_queryset().filter(age__gte=18)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
    #action to list students who are enrolled after 03/ 2026 only
    @action(detail=False, methods=["get"])
    def enrolled_after(self, request):
        qs = self.get_queryset().filter(enrollment_date__gt="2026-03-01")
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)



# Teacher
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# Class
class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer