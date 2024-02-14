from django.urls import path, include
from .views import *;

urlpatterns = [
  path('',sendmail,name="sendmail"),
  path('attachmentmail/',attachmentmail,name="attachmentmail"),
  path('dummymail/',dummymail,name='dummymail'),
  path('AttachMail/',sendattachmentmail,name='attachmail'),
  path('sentattachmail/',storemail,name='storemail'),
]