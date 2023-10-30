from django.db import models

# Create your models here.
class Instructor(models.Model):
    instructor_id = models.IntegerField(primary_key=True, default=1)  # Set a default value of 1
    name = models.CharField(max_length=255 , default='John Doe')
    department = models.CharField(max_length=255, default ='CSE')
    type = models.CharField(max_length=255, default='Permanent')
    salary = models.IntegerField(default=0)
    email = models.CharField(max_length=255, default='example@123')
    phone_number = models.CharField(max_length=12 ,default='9389040033')
    profile_picture = models.FileField(upload_to='profile_pics/' , default=' ')

class Research_by_faculty(models.Model):
    research_id = models.IntegerField(primary_key= True,default=1)
    research_area = models.CharField(max_length=100,null = False)
    status = models.CharField(max_length=100,default='active')
    budget = models.CharField(max_length=100,default='')
    research_topic = models.CharField(max_length=100,null=False)
    research_department = models.CharField(max_length=100,null=False)
 
class Researcher(models.Model):
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=False)
    research_id=models.ForeignKey(Research_by_faculty, on_delete=models.CASCADE)

class Publications(models.Model):
    publication_id = models.IntegerField(primary_key=True,default=1)
    publication_date = models.DateField()
    research_id = models.ForeignKey(Research_by_faculty, on_delete=models.CASCADE, null=False)
    publication_type = models.CharField(max_length = 100,  null=False)
    publication_link=models.CharField(max_length=100000, null=False, default="")      

class Courses(models.Model):
    course_id = models.IntegerField(primary_key=True,default=1)
    course_name = models.CharField(max_length=255,null=False)
    course_department = models.CharField(max_length=255,null=False)

class Teaches(models.Model):
    course_id = models.ForeignKey(Courses,on_delete=models.CASCADE, null=False)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=False)
    batch_year = models.IntegerField(max_length=255,null=False)
    semester = models.IntegerField(max_length=255,null=False)

class Specialization(models.Model):
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=False)
    Specialization = models.CharField(max_length=255)

class Awards(models.Model):
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=False)
    award_name = models.CharField(max_length=255)
    award_date = models.DateField()
    award_reason = models.CharField(max_length=255)


