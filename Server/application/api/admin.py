from django.contrib import admin
from api.models import Instructor,Research_by_faculty,Publications,Researcher,Courses,Teaches
# Register your models here.

admin.site.register(Instructor)
admin.site.register(Research_by_faculty)
admin.site.register(Publications)
admin.site.register(Researcher)
admin.site.register(Courses)
admin.site.register(Teaches)
