from django.db import models

# Create your models here.

class Student(models.Model):  
    s_id = models.CharField(max_length=20)  
    s_name = models.CharField(max_length=100)
    s_lastname = models.CharField(max_length=100)
    s_street = models.CharField(max_length=100)
    s_city = models.CharField(max_length=100)
    s_district = models.CharField(max_length=100)
    s_state = models.CharField(max_length=100)
    s_pin = models.CharField(max_length=10)
    s_class = models.CharField(max_length=100)
    s_section = models.CharField(max_length=100)
    s_dob = models.DateField()
    s_gender = models.CharField(max_length=100)
    s_father_name = models.CharField(max_length=100)
    s_mother_name = models.CharField(max_length=100)
    s_fathers_occupation = models.CharField(max_length=100)
    s_fmobile_number = models.CharField(max_length=15)
    s_fathers_email = models.EmailField(max_length=100)
    s_password = models.CharField(max_length=25)  
    class Meta:  
        db_table = "Student" 
        
        

class Teacher(models.Model):  
    t_id = models.CharField(max_length=20)  
    t_name = models.CharField(max_length=100)
    t_lastname = models.CharField(max_length=100)
    t_street = models.CharField(max_length=100)
    t_district = models.CharField(max_length=100)
    t_state = models.CharField(max_length=100)
    t_pin = models.CharField(max_length=10)
    t_section = models.CharField(max_length=100)
    t_dob = models.DateField()
    t_gender = models.CharField(max_length=100)
    t_mobile = models.CharField(max_length=15)
    t_email = models.EmailField(max_length=100)
    t_adhar = models.CharField(max_length=100)
    t_doj = models.DateField(max_length=100)
    t_password = models.CharField(max_length=25)  
    class Meta:  
        db_table = "Teacher"