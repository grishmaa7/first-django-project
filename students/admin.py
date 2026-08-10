from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "age"]
    search_fields = ["name"]
    list_filter = ["class_name"]

admin.site.register(Student, StudentAdmin)  #module register garna ko lagi
