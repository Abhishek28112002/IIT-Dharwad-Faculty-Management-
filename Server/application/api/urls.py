from django.contrib import admin
from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "IITDH-FACULTY-AFFAIRS ADMIN"
admin.site.site_title = "IITDH-FACULTY-AFFAIRS PORTAL ADMIN"


urlpatterns = [
    path("", views.index ,name='home'),
    path('admin/', admin.site.urls),

    path('instructors/', views.All_faculty, name='instructor_list'),
    path('All_Research',views.All_Research , name = 'All_Research'),
    path('All_Publications',views.All_Publications,name='All_Publications'),

    path('department_sorted_instructors' , views.Faculty_by_deaprtment , name ='department_sorted_instructors'),
    path('Faculty_by_deaprtment_research' , views.Faculty_by_deaprtment_research, name='Faculty_by_deaprtment_research'),

    path('add_faculty',views.add_faculty,name = 'add_faculty'),
    path('add_publication',views.add_publication,name='add_publication'),
    path('add_reaserch',views.add_reaserch,name='add_reaserch'),

    # path('personal_information', views.personal_info,name='personal_info'),
    path('sigin',views.sigin,name='sigin'),
    path('signup',views.signup,name='signup'),

    path('get_csrf_token/', views.get_csrf_token, name='get_csrf_token'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)