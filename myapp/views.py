from django.shortcuts import render

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