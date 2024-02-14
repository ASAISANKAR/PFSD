import csv
import os


import requests
from django.core.mail import send_mail, message,EmailMessage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#1st One
def sendmail(request):
    csv_file_path =r'D:\2nd Year 2nd Sem\PFSD\Python\pythonProject\Django_Project\TTM\PFSD\static\CSV.csv'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUians'  # Set your subject here
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

#2nd One
def attachmentmail(request):
    csv_file_path = r'D:\2nd Year 2nd Sem\PFSD\Python\pythonProject\Django_Project\TTM\PFSD\static\CSV.csv'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Email Attachment in Django Project'
            message_body = 'Hey, Check the Attachment'
            try:
                mail = EmailMessage(subject=subject, body=message_body, from_email='saisankar3193@gmail.com', to=[recipient_email],cc=['asankar2004@gmail.com'])
                mail.attach_file(r'static\CSV.csv')
                mail.attach_file(r'static\dummy.pdf')
                mail.send()
            except ArithmeticError as aex:
                print(aex.args)
                return HttpResponse('Invalid header found')
    return HttpResponse("Mail Sent Successfully")


#3rd One
def dummymail(request):
    recipient_email = 'asankar2004@gmail.com'
    subject = 'Email Attachment in Django Project'
    message_body = 'Hey, Check the Attachment'
    try:
        mail = EmailMessage(subject=subject, body=message_body, from_email='saisankar3193@gmail.com',
                            to=[recipient_email], cc=['asankar2004@gmail.com'])
        file_path = 'static/file.xlsx'
        file_url = 'https://docs.google.com/spreadsheets/d/1jFlUjTEYD2Z56a8NiicOGFQJH16ujs3d_ShMtD3J-JY/export?format=xlsx'
        response = requests.get(file_url)
        with open(file_path, 'wb') as f:
            f.write(response.content)

        mail.attach_file(r'static\file.xlsx')
        mail.send()
        os.remove(file_path)
    except ArithmeticError as aex:
        print(aex.args)
        return HttpResponse('Invalid header found')


    return HttpResponse("Mail Sent Successfully")


def sendattachmentmail(request):
    return render(request,'Attachmentmail.html')


from django.http import HttpResponse
from django.core.mail import EmailMessage
import csv

#4th One
def storemail(request):
    if request.method == "POST":
        docu=request.POST['attach']
        csv_file_path = r'D:\2nd Year 2nd Sem\PFSD\Python\pythonProject\Django_Project\TTM\PFSD\static\CSV.csv'

        file_path1='static/files.xlsx'
        file_url1=docu
        response1=requests.get(file_url1)
        with open(file_path1,'wb')as f:
            f.write(response1.content)



        with open(csv_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                recipient_email = row['email']
                subject = 'Email Attachment in Django Project'
                message_body = 'Hey, Check the Attachment'
                try:
                    mail = EmailMessage(subject=subject, body=message_body, from_email='saisankar3193@gmail.com',
                                        to=[recipient_email], cc=['asankar2004@gmail.com'])
                    print(f'Sent email to {recipient_email}')
                    mail.attach_file(file_path1)
                    mail.send()
                except ArithmeticError as aex:
                    print(aex.args)
                    return HttpResponse('Invalid header found')
        return HttpResponse("Mail Sent Successfully")








