from django.http import HttpResponse
from django.shortcuts import render
from prog3app.models import student, course, projectForm, projectReg

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

