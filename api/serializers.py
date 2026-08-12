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


    #objject level validation
    def validate(self, data):
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError(
                "Start date must be before end date."
            )
        return data  #always return it
    name = serializers.CharField(
        required=True, min_length=2,
        error_messages={
            "required": "Name is required.",
            "min_length": "Name must be at least 2 characters long.",
        },
    )


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
    def validate_age(self, value):
        if value < 5:
            raise serializers.ValidationError("Age must be at least 5.")
        return value  #always return it
        # The server controls these -- clients can't set them.
        read_only_fields = ["id", "enrollment_date"]

    name = serializers.CharField(
        required=True, min_length=2,
        error_messages={
            "required": "Name is required.",
            "min_length": "Name must be at least 2 characters long.",
        },
    )


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        
        fields = ["id", "name", "subject", "email", "hire_date"]

        # The server controls this -- clients can't set it.
        read_only_fields = ["id"]

    name = serializers.CharField(
        required=True, min_length=2,
        error_messages={
            "required": "Name is required.",
            "min_length": "Name must be at least 2 characters long.",
        },
    )