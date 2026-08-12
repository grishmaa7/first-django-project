from rest_framework.generics import (
     ListCreateAPIView, 
     RetrieveUpdateDestroyAPIView,
)

from students.models import Student
from classes.models import Class
from teacher.models import Teacher
from api.serializers import (
    StudentSerializer,
    ClassSerializer,
    TeacherSerializer,
)

#student APIs

class StudentListAPI(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get_queryset(self):
        students = Student.objects.select_related("class_name").all()

        class_id = self.request.query_params.get("class_id")
        if class_id:
            students = students.filter(class_name_id=class_id)

        return students

    


class StudentDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#class APIs
class ClassListAPI(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    #filter how many classes in 3 months
    def get_queryset(self):
        classes = Class.objects.all()

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")

        if start_date and end_date:
            classes = classes.filter(start_date__gte=start_date, end_date__lte=end_date)

        return classes

class ClassDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer





#teacher APIs
class TeacherListAPI(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

