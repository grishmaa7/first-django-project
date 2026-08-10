from django import forms
from students.models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# --------------------------------------------------------
# A plain Form (NOT tied to a model). Used for the Contact page.
# It shows form fields, built-in validation, and one custom rule.
# --------------------------------------------------------
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        min_length=2,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    phone_number = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}),
    )

    # Custom validation for ONE field: name the method clean_<field name>.
    def clean_name(self):
        name = self.cleaned_data["name"]
        if name.lower() == "admin":
            raise forms.ValidationError("Please use your real name.")
        return name              # always return the value if it's OK

    # Custom validation for phone_number: must be exactly 10 digits.
    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain digits only.")
        if len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        return phone_number

        # always return the value if it's OK

# --------------------------------------------------------
# A ModelForm. It builds its fields automatically from the Student model.
# Used to ADD and EDIT students.
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "age", "class_name"]
        labels = {"class_name": "Class"}
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "class_name": forms.Select(attrs={"class": "form-control"}),
        }

    # Custom validation: age must be at least 5
    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 5:
            raise forms.ValidationError("Age must be 5 or older.")
        return age

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )