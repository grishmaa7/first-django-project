from django.db import models
from classes.models import Class


# A Student belongs to one Class (a ForeignKey = many students -> one class).
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    class_name = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="students",
    )
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Students"
