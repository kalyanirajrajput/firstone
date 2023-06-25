from django.shortcuts import render,redirect
from FormApp.models import Register
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "home.html",{})


def Registration(request):
    if (request.method=="GET"):
        return render(request, "registration.html",{})
    else:
        uname=request.POST["uname"]
        dob = request.POST["dob"]
        course = request.POST["course"]
        location = request.POST["location"]
        pwd=request.POST["pwd"]
        try:
            student = Register.objects.get(UserName=uname,Password=pwd)
        except:
            user = Register()
            user.UserName = uname
            user.DOB = dob
            user.CourseName = course
            user.Location = location
            user.Password = pwd
            user.save()
            return redirect(home)            
        else:
            message= "This user is already present please try with another 'MOB NO.' !!!"
            return render(request, "registration.html",{})



def Login(request):
    if (request.method=="GET"):
        return render(request, "login.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]  
    try:
        user = Register.objects.get(UserName=uname,Password=pwd)
        
    except:
        msg="Enter valid User Name and Password"
        return render(request, "Login.html",{"msg":msg})
    else:
        return render(request, "showdetails.html",{"user":user})
    

     