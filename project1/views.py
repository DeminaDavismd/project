from django.shortcuts import render
from django.http import HttpResponse
from.models import Departmentss,Doctor
from .forms import appointmetForms,contactForms

# Create your views here.
def index(request):
    numbers={
        'num':['banana','apple','grapes']
    }
    
    return render(request,'index.html',numbers)

def about(request):
    
    
    return render(request,'about.html')
def contact(request):
    
    if request.method == "POST":
       form =contactForms(request.POST)
       if form.is_valid():
           form.save()   
           return render(request,'query.html')
    form=contactForms()
    dict_contact={
        'form':form
    }
    return render(request,'contact.html',dict_contact)
def Department(request):
    dict_dept={
    'dept':Departmentss.objects.all()
    }
    return render(request,'Department.html',dict_dept)
def doctors(request):
    dict_doc={
    'Doctor':Doctor.objects.all()
    }

    return render(request,'doctors.html',dict_doc)
def booking(request):
    if request.method == "POST":
       form =appointmetForms(request.POST)
       if form.is_valid():
           form.save()   
           return render(request,'confirmation.html')
    form=appointmetForms()
    dict_form={
        'form':form
    }
 
    return render(request,'booking.html',dict_form)