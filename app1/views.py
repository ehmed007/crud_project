from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import student_registration
from .models import Student
# Create your views here.

def home(request):      
    fm = student_registration()
    data = Student.objects.all()
    return render(request, 'app1/home.html',{'data':data,'form':fm})


def add_student(request):
    if request.method == 'POST':
        fm = student_registration(request.POST)
        if fm.is_valid():
            entry = Student(request.POST)
            entry = Student(name=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
            entry.save()
    return HttpResponseRedirect('/')


def edit_student(request, stu_id):
    print(request.method)
    if request.method == 'POST':
        print('ahmed')
        d = Student.objects.get(pk=stu_id)
        d.name = request.POST['name']
        d.email = request.POST['email']
        d.password =  request.POST['password']
        d.save()
        fm = student_registration()
    else:
        d = Student.objects.get(pk=stu_id)
        fm = student_registration(instance=d)        
    
    return render(request, 'app1/edit.html',{'form':fm})


def del_student(request, stu_id):
    if request.method == 'POST':
        print(request.method)
        pi = Student.objects.get(pk=stu_id)
        pi.delete()        

    return HttpResponseRedirect('/')    