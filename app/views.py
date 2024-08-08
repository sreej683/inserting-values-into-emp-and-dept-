from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def htmlforms(request):
    if request.method=='POST':
        return HttpResponse('Post is created')
    return render(request,'htmlforms.html')




def insert_dept(request):
    if request.method=='POST':
        deptno=request.POST['deptno']
        dname=request.POST['dname']
        dloc=request.POST['dloc']
        DO=Dept.objects.get_or_create(deptno=deptno,dname=dname,dloc=dloc)[0]
        DO.save()
        return HttpResponse('dept is created')
    return render(request,'insert_dept.html')



def insert_emp(request):
    EMO=Dept.objects.all()
    d={'EMO':EMO}
    return render(request,'insert_emp.html',d)
