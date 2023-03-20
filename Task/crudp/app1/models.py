from django.db import models

# Create your models here.
class Student(models.Model):
    input = models.CharField(max_length=50)
    