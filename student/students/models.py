
from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    total_marks = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
