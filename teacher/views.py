
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from teacher.models import Teacher

@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/list.html", {"teachers": teachers})

@login_required
def teacher_detail(request, id):
    teacher = Teacher.objects.get(id=id)
    return render(request, "teachers/detail.html", {"teacher": teacher})