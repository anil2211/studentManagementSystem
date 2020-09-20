from django.shortcuts import render, redirect  
from .forms import StudentForm,TeacherForm 
from .models import Teacher,Student 

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')
 
def studentpage(request):
    return render(request,'student.html')
 
def addstudent(request):
    return render(request,'indexsms.html')
     
def stu(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'indexsms.html',{'form':form})


# def stu(request):
#     obj=Student()
#     # obj.s_id=request.POST['s_id']
#     obj.s_name=request.POST['s_name']
#     obj.s_lastname=request.POST['s_lastname']
#     obj.s_street=request.POST['s_street']
#     obj.s_city=request.POST['s_city']
#     obj.s_district=request.POST['s_district']
#     obj.s_state=request.POST['s_state']
#     obj.s_pin=request.POST['s_pin']
#     obj.s_class=request.POST['s_class']
#     obj.s_section=request.POST['s_section']
#     obj.s_dob=request.POST['s_dob']
#     obj.s_gender=request.POST['s_gender']
#     obj.s_father_name=request.POST['s_father_name']
#     obj.s_mother_name=request.POST['s_mother_name']
#     obj.s_fathers_occupation=request.POST['s_fathers_occupation']
#     obj.s_fmobile_number=request.POST['s_fmobile_number']
#     obj.s_fathers_email=request.POST['s_fathers_email']
#     obj.s_password=request.POST['s_password']
#     obj.save()
#     return render (request,'indexsms.html',{'detail':'succesfully submit '})

def show(request):  
    students = Student.objects.all()  
    return render(request,"show.html",{'students':students})


def edit(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'edit.html', {'student':student}) 

def update(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'student':student})


def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/show")  








