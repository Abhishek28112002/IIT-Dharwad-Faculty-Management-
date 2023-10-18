from django.contrib import admin
from django.urls import path
from api import views



admin.site.site_header = "IITDH-FACULTY-AFFAIRS ADMIN"
admin.site.site_title = "IITDH-FACULTY-AFFAIRS PORTAL ADMIN"


urlpatterns = [
    path("", views.index ,name='home'),
    path('admin/', admin.site.urls),
   path('instructors/', views.All_faculty, name='instructor_list'),
    path("admin_page" , views.add , name = 'add'),
    path('department_sorted_instructors' , views.Faculty_by_deaprtment , name ='department_sorted_instructors'),
]