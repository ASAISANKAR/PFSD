# myapp/urls.py
from django.urls import path
from .views import *


urlpatterns = [
   path('hello1/',hello1,name="Hello1"),
   path('',newhomepage,name='newhomepage'),
   path('time1',time11,name='time1'),
   path('travelpackage/',travelpackage,name='travelpackage'),
   path('print/',print1,name='print'),
   path('s/',print_to_console,name='print_to_console'),
   path('otp1/',otp,name='Otpgenerate'),
   path('myteam/',myteam,name='myteam'),
   path('date_time/',getdate1,name='date_time'),
   path('date_time1/',get_date,name='date_time1'),
   path('register/',register,name='register'),
   path('registerloginfunction',registerloginfunction,name='registerloginfunction'),
   path('admin/',admin,name='admin'),
   path('loginpage/',loginpage,name='loginpage'),
   path('login/',login,name='login'),
   path('user/',user,name='user'),
   path('cars/',cars,name='cars'),
   path('weather/',weatherpage,name='weather'),
   path('weatherlogic',weatherlogic,name='weatherlogic'),
   path('feedback/',feedbackform,name='feedback'),
   path('feedbacksave/',feedbacksave,name='feedbacksave'),

]