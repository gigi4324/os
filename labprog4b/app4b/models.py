from django.db import models
from django.forms import ModelForm

# Create your models here.
class course(models.Model):
    courseCode = models.CharField(max_length=10)
    courseName = models.CharField(max_length=50)
    courseCredits = models.IntegerField()

    def __str__(self):
        return self.courseCode + " " + self.courseName + " " + str(self.courseCredits)

class student(models.Model):
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    sem = models.IntegerField()
    courses = models.ManyToManyField(course, related_name='student_set')

    def __str__(self):
        return self.usn + " " + self.name + " " + str(self.sem)

class projectReg(models.Model):
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    ptitle=models.CharField(max_length=30)
    planguage=models.CharField(max_length=30)
    pduration=models.IntegerField()
    
    
class projectForm(ModelForm): 
    required_css_class="required" 
    class Meta: 
        model=projectReg 
        fields=['student','ptitle','planguage','pduration'] 
        
        


