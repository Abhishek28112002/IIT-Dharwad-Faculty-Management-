from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection



def All_faculty(request):
   with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM api_instructor")  
        instructors = cursor.fetchall()
   return HttpResponse(instructors, content_type='text/plain')
    
def Faculty_by_deaprtment(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT department, array_agg(name) as instructors FROM api_instructor GROUP BY department")
        instructors = cursor.fetchall()
    return HttpResponse(instructors, content_type='text/plain')

def index(request):
    return HttpResponse("helloo world")

def add(request):
    if(request.method == "POST"):
        instructor_id = request.POST.get('instructor_id')
        name = request.POST.get('name')
        department = request.POST.get('department')
        type = request.POST.get('type') 
        salary = request.POST.get('salary')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        performance_score = request.POST.get('performance_score')
        Instructor = Instructor(name = name , email=email, instructor_id = instructor_id ,department= department,type = type, salary= salary,phone_number= phone_number,performance_score=performance_score)
        Instructor.save()
    return render(request , 'admin_page.html')

def __str__(self):
    return self.instructor_id