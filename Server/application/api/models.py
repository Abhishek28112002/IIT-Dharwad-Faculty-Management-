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
    performance_score = models.IntegerField(default=0)


 