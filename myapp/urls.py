"""
URL configuration for employee_mangt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='index'),
    path("register/",views.userreg, name='userreg'),
    path("insertuser/",views.insertuser, name='insertuser'),
    path("viewuser/",views.viewuser, name='viewuser'),
    path("deleteuser/<int:id>", views.deleteuser,name='deleteuser'),
    path("edituser/<int:id>/", views.edituser,name='edituser'),  #end / bcz of post method
    path("updateuser/<int:id>/", views.updateuser,name='updateuser'), #end / bcz of post method
    path('upload_excel', views.upload_excel, name='upload_excel'),
    path('view_data', views.view_excel, name='view_data'),
    path('about', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('send_contact_email/', views.send_contact_email, name='send_contact_email'),  # Email sending


]
