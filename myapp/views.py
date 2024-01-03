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
from django.shortcuts import render
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
