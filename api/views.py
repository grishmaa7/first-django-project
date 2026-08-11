from rest_framework import status
from rest_framework.views import APIView
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


class HelloAPI(APIView):
    def get(self, request):
        return Response({"message": "Hewwoooo world!"}, status=status.HTTP_200_OK)


class StudentListAPI(APIView):
    """
    List all students, or create a new student.
    """
    def get(self, request):
        # select_related -> the Class is gotten in 1 query, it stops the API
        # running one extra query per student for the nested Class data
        students = Student.objects.select_related("class_name").all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailAPI(APIView):

    def get(self, request, id):        # RETRIEVE
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):        # UPDATE
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(
            student, data=request.data
        )  # instance + data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):     # DELETE
        Student.objects.get(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClassListAPI(APIView):
    """
    List all classes, or create a new class.
    """
    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassDetailAPI(APIView):

    def get(self, request, id):        # RETRIEVE
        class_obj = Class.objects.get(id=id)
        serializer = ClassSerializer(class_obj)
        return Response(serializer.data)

    def put(self, request, id):        # UPDATE
        class_obj = Class.objects.get(id=id)
        serializer = ClassSerializer(
            class_obj, data=request.data
        )  # instance + data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):     # DELETE
        Class.objects.get(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherListAPI(APIView):
    """
    List all teachers, or create a new teacher.
    """
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailAPI(APIView):

    def get(self, request, id):        # RETRIEVE
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):        # UPDATE
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(
            teacher, data=request.data
        )  # instance + data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):     # DELETE
        Teacher.objects.get(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)