# myapp/urls.py
from django.urls import path
from .views import *


urlpatterns = [
   path('hello1/',hello1,name="Hello1"),
   path('',newhomepage,name='newhomepage'),
   path('travelpackage/',travelpackage,name='travelpackage'),
   path('print/',print1,name='print'),
   path('s',print_to_console,name='print_to_console'),
]