import csv

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sendmail(request):
    csv_file_path =r'D:\2nd Year 2nd Sem\PFSD\Python\pythonProject\Django_Project\TTM\PFSD\static\CSV.csv'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, Welcome to PFSD Class, Hope u have a great time with python'  # Set your email content here
            send_mail(
                subject,
                message_body,
                'saisankar3193@gmail.com',
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
    return HttpResponse("Mail Sent Successfully")