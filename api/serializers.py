from rest_framework import serializers
from students.models import Student
from classes.models import Class
from teacher.models import Teacher


# A small serializer for Class
# StudentSerializer for Class uses this as a nested inside
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["id", "name", "description", "start_date", "end_date"]


class StudentSerializer(serializers.ModelSerializer):
    # Nested (read-only), shows the whole class object when reading.
    class_detail = ClassSerializer(source="class_name", read_only=True)

    class Meta:
        model = Student

        # "class_name" (the id) is used when WRITING.
        # "class_detail" (the object) is what you get when READING.
        fields = [
            "id",
            "name",
            "email",
            "age",
            "class_name",
            "class_detail",
            "enrollment_date",
        ]

        # The server controls these -- clients can't set them.
        read_only_fields = ["id", "enrollment_date"]


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "name", "subject", "email", "hire_date"]

        # The server controls this -- clients can't set it.
        read_only_fields = ["id"]