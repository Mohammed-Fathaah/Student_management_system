from django.db import models

# Create your models here.
class Student(models.Model):
    roll=models.IntegerField(unique=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    department=models.CharField(max_length=100)
    mark=models.IntegerField()

    def __str__(self):
        return self.name