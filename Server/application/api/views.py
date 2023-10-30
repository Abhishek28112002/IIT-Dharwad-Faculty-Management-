from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.db import connection
from django.middleware.csrf import get_token
import json

#all faculty apis
def All_faculty(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT instructor_id,name,department,type,salary,email,phone_number FROM api_instructor")
        instructors = cursor.fetchall()

    instructors_data = []
    for instructor in instructors:
        instructor_dict = {
            'instructor_id': instructor[0],
            'name': instructor[1],
            'department': instructor[2],
            'type': instructor[3],
            'salary': instructor[4],  
            'email': instructor[5],  
            'phone_number': instructor[6],
        }
        instructors_data.append(instructor_dict)

    return HttpResponse(json.dumps(instructors_data), content_type='application/json')
    
    
def Faculty_by_deaprtment(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT instructor_id, name, department, type, salary,  email, phone_number FROM api_instructor ORDER BY department")
        instructors = cursor.fetchall()
    
    instructors_data = []
    for instructor in instructors:
        instructor_dict = {
            'instructor_id': instructor[0],
            'name': instructor[1],
            'department': instructor[2],
            'type': instructor[3],
            'salary': instructor[4],  
            'email': instructor[5],  
            'phone_number': instructor[6],
        }
        instructors_data.append(instructor_dict)
    return HttpResponse(json.dumps(instructors_data), content_type='text/plain')


# def Faculty_by_performance_score(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT performance_score, ARRAY_AGG(email) as email, ARRAY_AGG(instructor_id) as instructor_id, ARRAY_AGG(name) as name, ARRAY_AGG(salary) as salary, ARRAY_AGG(phone_number) as phone_number , ARRAY_AGG(department) as department , ARRAY_AGG(type) as type  FROM api_instructor GROUP BY performance_score")
#         instructors = cursor.fetchall()
    
#     instructors_data = []
#     for instructor in instructors:
#         instructor_dict = {
#             'department': instructor[0],
#             'email': instructor[1],
#             'instructor_id': instructor[2],
#             'name': instructor[3],
#             'salary': instructor[4],  
#             'phone_number': instructor[5],  
#             'performance_score': instructor[6],
#             'type' :instructor[7],
#         }
#         instructors_data.append(instructor_dict)
#     return HttpResponse(json.dumps(instructors_data), content_type='text/plain')
def add_faculty(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        department = data.get('department')
        email = data.get('email')
        instructor_id = data.get('instructor_id')
        name = data.get('name')
        salary = data.get('salary')
        phoneNo = data.get('phoneNo')
        type = data.get('type')

        with connection.cursor() as cursor:
            insert_query = "INSERT INTO api_instructor (department, email, instructor_id, name, salary, phoneNo, type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, [department, email, instructor_id, name, salary, phoneNo, type])
            cursor.commit()
    else:
        print('Tumse na ho payega')


def Edit_faculty(request):
    if(request.method == 'PUT'):
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        profile_pic = data.get('profile_pic')
        department = data.get('department')
        password = data.get('password')
        phone_number = data.get('phone_number')
    with connection.cursor() as cursor:
        update_query = "update api_instructor set name=%s,email=%s,profile_pic=%s,department=%s,password=%s,phone_number=%s"
        cursor.execute(update_query,[name,email,profile_pic,department,password,phone_number])
    return JsonResponse({'data edited successfully'})

# def Delete_faculty(request):
#     if(request.method == 'DELETE'):
#         data = json.loads(request.body)
#         instructor_id = data.get('instructor_id')
#     with connection.cursor() as cursor:
#         Delete_query = "delete from api_instructor where instructor_id = %s"
#         cursor.execute(Delete_query , [instructor_id])
#     return JsonResponse({'data has been deleted'})



# research apis

def All_Research(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT research_id ,research_area, status, budget ,research_topic, research_department FROM api_research_by_faculty")
        research = cursor.fetchall()

    research_data = []
    for each_research in research:
        research_dict = {
            'research_id': each_research[0],
            'research_area': each_research[1],
            'status': each_research[2],     
            'research_topic' :each_research[3],
            'research_department' :  each_research[4],
        }
        research_data.append(research_dict)
    return HttpResponse(json.dumps(research_data), content_type='text/plain')


def Faculty_by_deaprtment_research(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT  status, research_area, budget,research_topic,research_department FROM api_Research_by_faculty ORDER BY research_department")
        research = cursor.fetchall()
    
    research_data = []
    for each_research in research:
        research_dict = {
            'status': each_research[0],
            'research_area': each_research[1],
            'budget': each_research[2], 
            'research_topic' :each_research[3],
            'research_department' :  each_research[4],
        }
        research_data.append(research_dict)
    return HttpResponse(json.dumps(research_data), content_type='text/plain')

def add_reaserch(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        status = data.get('status')
        research_area = data.get('research_area')
        budget = data.get('budget')
        research_topic = data.get('research_topic')
        research_department= data.get('research_department')
    with connection.cursor() as cursor:
        insert_query = "insert into api_Research_by_faculty(status,research_area,budget,research_topic,research_department) value(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_query,[status,research_area,budget,research_topic,research_department])
    return JsonResponse({'data inserted successfully'})

def Edit_Research(request):
    if(request.method == 'PUT'):
        data = json.loads(request.body)
        research_topic = data.get('research_topic')
        research_area = data.get('research_area')
        status = data.get('status')
        professor = data.get('professor')
        budget = data.get('budget')
    with connection.cursor() as cursor:
        update_query = "update api_Research_by_faculty set research_topic=%s,research_area=%s,status=%s,professor=%s,budget=%s"
        cursor.execute(update_query,[research_topic,research_area,status,professor,budget])
    return JsonResponse({'data edited successfully'})

# publications api 
# def Faculty_by_deaprtment_publications(request):
#     with connection.cursor() as cursor:
#         cursor.execute("")
#         publications = cursor.fetchall()
    
#     publications_data = []
#     for each_publication in publications:
#         publications_dict = {
#             'publication_id': each_publication[0],
#             'instructor_id': each_publication[1],
#             'title': each_publication[2],     
#             'publication_date' :each_publication[3],
#             'research_paper_id' :  each_publication[4],
#             'publication_type' : each_publication[5]
#         }
#         publications_data.append(publications_dict)
#     return HttpResponse(json.dumps(publications_data), content_type='text/plain')

def All_Publications(request):
    with connection.cursor() as cursor:
        query = "SELECT  array_agg(distinct api_Research_by_faculty.research_department) as department,  api_Research_by_faculty.research_topic as title,  array_agg(distinct api_Publications.publication_date) as publication_dates,  array_agg(distinct api_Publications.publication_type) as publication_type, array_agg(distinct api_Publications.publication_link) as publication_link,  array_agg(distinct api_Instructor.name) as name, array_agg(distinct api_Researcher.research_id_id) as research_id FROM api_Instructor INNER JOIN api_Researcher ON api_Instructor.instructor_id = api_Researcher.instructor_id_id INNER JOIN api_Publications ON api_Researcher.research_id_id = api_Publications.research_id_id INNER JOIN api_Research_by_faculty ON api_Research_by_faculty.research_id = api_Publications.research_id_id GROUP BY api_Research_by_faculty.research_topic"
        cursor.execute(query)
        publications = cursor.fetchall()
    
    publications_data = []
    for each_publication in publications:
        publications_dict = {
            'department': each_publication[0],
            'title': each_publication[1],
            'publication_dates': [date.isoformat() for date in each_publication[2]],     
            'publication_type' : each_publication[3],
            'publication_link' :  each_publication[4],
            'name' : each_publication[5],
            'research_id': each_publication[6]
        }
        publications_data.append(publications_dict)
        serialized_data = json.dumps(publications_data)
    return HttpResponse(serialized_data, content_type='text/plain') 

    
def add_publication(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        publication_id = data.get('publication_id')
        instructor_id = data.get('instructor_id')
        title = data.get('title')
        publication_date = data.get('publication_date')
        research_paper_id= data.get('research_paper_id')
        publication_type = data.get('publication_type')
    with connection.cursor() as cursor:
        insert_query = "insert into api_Publications(publication_id,instructor_id,title,publication_date,research_paper_id,publication_type) value(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_query,[publication_id,instructor_id,title,publication_date,research_paper_id,publication_type])
    return JsonResponse({'data inserted successfully'})

def Edit_Publication(request):
    if(request.method == 'PUT'):
        data = json.loads(request.body)
        publication_id = data.get('publication_id')
        instructor_id = data.get('instructor_id')
        title = data.get('title')
        publication_date = data.get('publication_date')
        research_paper_id = data.get('research_paper_id')
        publication_type = data.get('publication_type')
    with connection.cursor() as cursor:
        update_query = "update api_Publications set publication_id=%s,instructor_id=%s,title=%s,publication_date=%s,research_paper_id=%s,publication_type=%s"
        cursor.execute(update_query,[publication_id,instructor_id,title,publication_date,research_paper_id,publication_type])
    return JsonResponse({'data edited successfully'})


#search functionality

def search_name_email(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        input = data.get('search')
    with connection.cursor() as cursor:
        search_query = "select * from api_instructor where name like %s or email like %s"
        cursor.execute(search_query,['%' + input + '%'])
        instructors = cursor.fetchall()
    
    instructors_data = []
    for instructor in instructors:
        instructor_dict = {
            'department': instructor[0],
            'email': instructor[1],
            'instructor_id': instructor[2],
            'name': instructor[3],
            'salary': instructor[4],  
            'phone_number': instructor[5],  
            'performance_score': instructor[6],
            'type' :instructor[7],
        }
        instructors_data.append(instructor_dict)
    return HttpResponse(json.dumps(instructors_data), content_type='text/plain')

def search_research(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        input = data.get('search')
    with connection.cursor() as cursor:
        search_query = "select * from api_Research_by_faculty where research_topic like %s"
        cursor.execute(search_query,['%' + input + '%'])
        research = cursor.fetchall()
    
    research_data = []
    for each_research in research:
        research_dict = {
            'status': each_research[0],
            'research_area': each_research[1],
            'budget': each_research[2],     
            'research_topic' :each_research[3],
            'research_department' :  each_research[4],
        }
        research_data.append(research_dict)
    return HttpResponse(json.dumps(research_data), content_type='text/plain')

def search_publications(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        input = data.get('search')
    with connection.cursor() as cursor:
        search_query = "select * from api_Publications where instructor_is in (select instructor_id from api_instructor where name like %s or email like %s)"
        cursor.execute(search_query,['%' + input + '%'])
        publications = cursor.fetchall()
    
    publications_data = []
    for each_publication in publications:
        publications_dict = {
            'publication_id': each_publication[0],
            'instructor_id': each_publication[1],
            'title': each_publication[2],     
            'publication_date' :each_publication[3],
            'research_paper_id' :  each_publication[4],
            'publication_type' : each_publication[5]
        }
        publications_data.append(publications_dict)
    return HttpResponse(json.dumps(publications_data), content_type='text/plain')

# def personal_info(request):
#      with connection.cursor() as cursor:
#        query = "select email,department,type,salary,phone_number from api_instructor"
#        cursor.execute(query)
#        information = cursor.fetchall()
    
#      personal_data = []
#      for data in information:
#         personal_dict ={
#             'email' : data[0],
#             'department' : data[1],
#             'type':data[2],
#             'salary':data[3],
#             'phone_number':data[4]
#         }
#         personal_data.append(personal_dict)
#      return HttpResponse(json.dumps(personal_data),content_type='text/plain')
    
#sigin , signup

def signup(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        print(data)
        name = data.get('name')
        email = data.get('email')
        department = data.get('department')
        password = data.get('password')
        phone_number = data.get('phoneNo')
    with connection.cursor() as cursor:
        insert_query = "insert into api_instructor(name,email,department,password,phone_number) values(%s,%s,%s,%s,%s)"
        cursor.execute(insert_query,[name,email,department,password,phone_number])
        connection.commit()
    return JsonResponse({'message': 'USER CREATED'})
    
def sigin(request):
    if(request.method == 'POST'):
        data = json.loads(request.body)
        email  = data.get('email')
        password = data.get('password')
    with connection.cursor() as cursor:
        get_query = "select * from api_instructor where email=%s,password=%s"
        cursor.execute(get_query,[email,password])
        user = cursor.fetchone()
    
    if user:
        return HttpResponse({'USER EXISTS'})
    else:
        return HttpResponse({'USER DOESNT EXISTS'})

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

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