# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('app/',include('crud_app.urls')),
    path('mail/',include('mailapp.urls')),
    path('reviews/',include('reviews.urls')),

]
