from django.shortcuts import render, redirect
from students.models import Student
from students.forms import ContactForm, StudentForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from students.forms import SignUpForm


# The home page of the whole site.

def home(request):
    print(request.user)  # shows the logged-in user in the console
    print(request.user.is_authenticated)  # True if logged in, False if not
    return render(request, "students/home.html")


# Show a list of all students.
def student_list(request):
    students = Student.objects.all()
    return render(request, "students/list.html", {"students": students})


# Show the details of one student (the id comes from the URL).
def student_detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, "students/detail.html", {"student": student})



# CONTACT page (a plain Form -- it does not save to a model).
def contact(request):
    sent = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # In a real app you would email this. Here we just say thanks.
            name = form.cleaned_data["name"]
            print(f"Thanks for your message, {name}!")
            sent = True
            form = ContactForm()          # reset to a blank form
    else:
        form = ContactForm()
    return render(request, "students/contact.html", {"form": form, "sent": sent})


 # ---------------------------------------------------------
# Class 5: adding, editing and deleting students with forms
# ---------------------------------------------------------

# ADD a new student (ModelForm)
@login_required
def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()                          # creates a new student row
            return redirect("students:list")
    else:
        form = StudentForm()                     # a blank form
    return render(request, "students/student_form.html", {"form": form, "title": "Add Student"})


# EDIT an existing student (same form + instance)
@login_required
def student_edit(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()                          # updates the existing student row
            return redirect("students:list")
    else:
        form = StudentForm(instance=student)     # pre-fill the form with this student's data
    return render(request, "students/student_form.html",
                   {"form": form, "title": "Edit Student"})

# DELETE an existing student
def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect("students:list")
    return render(request, "students/student_delete.html", {"student": student, "title": "Delete Student"})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  #creates the user 
            login(request, user)  #logs them in
            return redirect('students:home')
    else:
        form = SignUpForm()
    return render(request, 'students/signup.html', {'form': form})