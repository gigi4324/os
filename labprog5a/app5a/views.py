from django.http import HttpResponse
from django.shortcuts import render
from app5a.models import student, course, projectForm, projectReg

# Create your views here.
def home(request):
    return render(request, 'home.html')

def studentlist(request):
    s = student.objects.all()
    return render(request, 'studentlist.html', {'student_list': s})

def courselist(request):
    c = course.objects.all()
    return render(request, 'courselist.html', {'course_list': c})

def register(request):
    if request.method == "POST":
        sid = request.POST.get("student")
        cid = request.POST.get("course")
        studentobj = student.objects.get(id=sid)
        courseobj = course.objects.get(id=cid)
        res = studentobj.courses.filter(id=cid)
        if res:
            resp = "<h1>Student with usn %s has already enrolled for the %s<h1>" % (studentobj.usn, courseobj.courseCode)
            return HttpResponse(resp)
        studentobj.courses.add(courseobj)
        resp = "<h1>student with usn %s successfully enrolled for the course with sub code %s</h1>" % (studentobj.usn, courseobj.courseCode)
        return HttpResponse(resp)
    else:
        studentlist = student.objects.all()
        courselist = course.objects.all()
        return render(request, 'register.html', {'student_list': studentlist, 'course_list': courselist})

def enrolledStudents(request):
    if request.method == "POST":
        cid = request.POST.get("course")
        courseobj = course.objects.get(id=cid)
        studentlistobj = courseobj.student_set.all()
        return render(request, 'enrolledlist.html', {'course': courseobj, 'student_list': studentlistobj})
    else:
        courselist = course.objects.all()
        return render(request, 'enrolledlist.html', {'Course_List': courselist})
    
def add_project(request):
    if request.method=="POST":
        form=projectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Project Data Successfully saved</h1>")
        else:
            return HttpResponse("<h1>Project details not saved</h1>")
    else:
        form=projectForm()
        return render(request, "projectReg.html",{'form':form})
    
from django.views import generic
class StudentListView(generic.ListView):
    model=student
    template_name="GenericListViewStudent.html"
class StudentDetailView(generic.DetailView):
    model=student
    template_name="GenericDetailedViewStudent.html"
    

import csv
def generateCSV(request):
    courses=course.objects.all()
    resp=HttpResponse(content_type="text/csv")
    resp['Content-Disposition']='attachment; filename=course_data.csv'
    writer=csv.writer(resp)
    writer.writerow(['Course Code','Course Name','Course Credits'])
    for c in courses:
        writer.writerow([c.courseCode,c.courseName,c.courseCredits])
    return resp

from reportlab.lib.pagesizes import letter 
from reportlab.platypus import SimpleDocTemplate, Table
def generatePDF(request):
    courses=course.objects.all()
    resp=HttpResponse(content_type="text/pdf")
    resp['Content-Disposition']='attachment; filename=course_data.pdf'
    pdf=SimpleDocTemplate(resp,pagesize=letter)
    table_data=[['Course Code','Course Name','Course Credits']]
    for c in courses:
        table_data.append([c.courseCode,c.courseName,str(c.courseCredits)])
    table=Table(table_data)
    pdf.build([table])
    return resp

def registerajax(request):
    if request.method=="POST":
        sid=request.POST.get('usnid')
        cid=request.POST.get('ccodeid')
        studentobj=student.objects.get(id=sid)
        courseobj=course.objects.get(id=cid)
        res=studentobj.courses.filter(id=cid)
        if res:
            resp="<h1>Already Registered for this course</h1>"
            return HttpResponse(resp)
        studentobj.courses.add(courseobj)
        resp="<h1>Successfully Registered</h1>"
        return HttpResponse(resp)
    else:
        studentobjs=student.objects.all()
        courseobjs=course.objects.all()
        return render(request,'registerAJAX.html',{'studentList':studentobjs,'courseList':courseobjs})


