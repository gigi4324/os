"""
URL configuration for prog4proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app4.views import home, studentlist, courselist, register, enrolledStudents,add_project, StudentListView, StudentDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home),
    path('home/',home),
    path('studentlist/',studentlist),
    path('courselist/',courselist),
    path('register/',register),
    path('enrolledlist/',enrolledStudents),
    path('addproject/',add_project),
    path('genericlistviewstudent/',StudentListView.as_view()),
    path('genericdetailedviewstudent/<int:pk>/',StudentDetailView.as_view()),
]
