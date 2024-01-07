from django.shortcuts import render
import random,string
# Create your views here.
# myapp/views.py
from django.http import HttpResponse


def hello1(request):
    return HttpResponse("<center>Welcome to TTM Homepage</center>")

def newhomepage(request):
    return render(request,'NewHomePage.html')
def travelpackage(request):
    return render(request,'TravelPackage.html')

def print1(request):
    return render(request,'print_to_console.html')

def print_to_console(request):
    if request.method=="POST":
        user_input=request.POST['user_input']
        print(f'User input: {user_input}')
   # return HttpResponse('Form Submitted Successfully')
        a1={'user_input': user_input}
        return render(request,'print_to_console.html',a1)


def otp(request):
    ran1 = ''.join(random.sample(string.digits, k=4))
    print(f'OTP: {ran1}')
    a1 = {'ran1': ran1}
    return render(request,'Otpgenerate.html',a1)


def myteam(request):
    return render(request,'Myteam.html')


def getdate1(request):
    return render(request,'date_time.html')

import datetime
from django.shortcuts import render,redirect
from .forms import *
def get_date(request):
    if(request.method=='POST'):
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+datetime.timedelta(days=integer_value)
            return render(request,'date_time.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'date_time.html',{'form':form})


import time
def time11(request):

    time1=time.asctime()
    print(f'Time: {time1}')
    a1 = {'time1': time1}
    return render(request,'NewHomePage.html',a1)

def register(request):
    return render(request,'registerpage.html')

from .models import *

def registerloginfunction(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')

        if Sankar.objects.filter(email=email).exists():
            return HttpResponse("Email already registered. Choose a different email.")

        Sankar.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'registerpage.html')

def admin(request):
    return redirect('admin')