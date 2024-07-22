from django.db import models
from django.forms import ModelForm

# Create your models here.
class Course(models.Model):
    courseCode = models.CharField(max_length=10)
    courseName = models.CharField(max_length=50)
    courseCredits = models.IntegerField()

    def __str__(self):
        return self.courseCode + " " + self.courseName + " " + str(self.courseCredits)

class Student(models.Model):
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    sem = models.IntegerField()
    courses = models.ManyToManyField(Course, related_name='student_set')

    def __str__(self):
        return self.usn + " " + self.name + " " + str(self.sem)
