from django.shortcuts import render
from classes.models import Class


# Show a list of all classes.
def class_list(request):
    classes = Class.objects.all()
    return render(request, "classes/list.html", {"classes": classes})


# Show one class, plus the students enrolled in it.
def class_detail(request, id):
    single_class = Class.objects.get(id=id)
    return render(request, "classes/detail.html", {"single_class": single_class})
