from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .models import User, URLS
import pandas as pd
import openpyxl

# Create your views here.
def index(request):
    return render(request,"myapp/index.html")


def userreg(request):
    return render(request,"myapp/userreg.html" )

def insertuser(request):
    if request.method == 'POST':
        vuid = request.POST.get('tuid')
        vuname = request.POST.get('tuname')
        vuemail = request.POST.get('tuemail')
        vucontact = request.POST.get('tucontact')

        us = User(uid=vuid, uname=vuname, uemail=vuemail, ucontact=vucontact)
        us.save()

        # Redirect to success page after registration
        return redirect('index')  # Redirect to the success URL

    return render(request, 'myapp/userreg.html')  # Render the form for GET requests


def viewuser(request):
    user=User.objects.all()
    return render(request, "myapp/viewuser.html",{"userdata":user})


def deleteuser(request,id):
    us=User.objects.get(id=id) #delete single user which having id
    # us=User.objects.filter(id=id) #delete multiple user whose having same id
    us.delete()
    return redirect("/viewuser")

def edituser(request,id):
    user=User.objects.get(id=id)
    return render(request, "myapp/edituser.html",{"user":user})

def updateuser(request,id):
    if request.method == 'POST':
        newuid = request.POST.get('tuid')
        newuname = request.POST.get('tuname')
        newuemail = request.POST.get('tuemail')
        newucontact = request.POST.get('tucontact')
        us=User.objects.get(id=id)

        us.uid=newuid
        us.uname=newuname
        us.uemail=newuemail
        us.ucontact=newucontact
        us.save()

        # Redirect to success page after registration
        return redirect("/viewuser")
    
    return render(request, 'myapp/edituser.html') 


def upload_excel(request):
    if request.method == 'POST' and request.FILES['excelFile']:
        excel_file = request.FILES['excelFile']
        
        # Read the uploaded Excel file into a pandas DataFrame
        df = pd.read_excel(excel_file)
        # for index, row in df.iterrows():
        #     urlid=row['URL_ID']
        #     url=row["URL"]
        #     ur=URLS(urlid=urlid, url=url)
        #     ur.save()

        # Process the DataFrame or save it to the database as needed
        # For demonstration, we can display the DataFrame contents
        # return HttpResponse(df.to_html())  # Displays data as HTML table

    return render(request, 'myapp/upload_form.html')

def view_excel(request):
    df=URLS.objects.all()
    
    return render(request, 'myapp/upload_form.html',{"df":df})

def about(request):
    return render(request, "myapp/about.html")

def contactus(request):
    return render(request, "myapp/contactus.html")



def send_contact_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        message = request.POST.get('message')

        # Prepare email
        subject = 'Contact Form Submission from UMS'
        body = f'Name: {name}\nEmail: {email}\nContact: {contact}\nMessage: {message}'
        
        try:
            send_mail(subject, body, 'your_email@example.com', [email])
            messages.success(request, 'Thank you for contacting us! We will reply as soon as possible.')
            return redirect('contactus')  # Redirect to the contact page after sending
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')
    
    return render(request, 'myapp/index.html')





