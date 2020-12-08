from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def docs(request):
    return render(request,'docs.html')

def contact(request):
    if request.method=='POST':
        N=request.POST.get('name')
        E=request.POST.get('email')
        P=request.POST.get('phone')
        M=request.POST.get('message')
        D=datetime.today()
        contact=Contact(name=N,email=E,phone=P,message=M,date=D)
        contact.save()
    return render(request,'contact.html')

def auth(request):
    return render(request,'auth.html')

def confirmed(request):
    return render(request,'confirmed.html')