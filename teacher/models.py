from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
