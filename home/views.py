from django.shortcuts import render
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

    messages.success(request,"This is a test message")

def about(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save
        messages.success(request, "Your message has been send !")

    return render(request,'about.html')
    
def base(request):
    return render(request,'base.html')

def list(request):       
    return render(request,'list.html')    