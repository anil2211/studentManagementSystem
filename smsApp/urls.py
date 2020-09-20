from django.urls import path
from . import views
from django.contrib import admin  



urlpatterns = [  
    # path('admin/', admin.site.urls),  
    path('',views.index),
    path('home',views.home),
    path('stu', views.stu), 
    path('addstudent',views.addstudent),
    path('studentpage',views.studentpage), 
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]