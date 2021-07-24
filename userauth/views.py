from django import http
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http.request import HttpRequest 
from django.apps import apps
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def loginPage(request):
    return render(request,'userauth/login.html')

def registerPage(request):
    return render(request,'userauth/register.html')

@csrf_exempt
def registerHandle(request):

    if request.method=='POST':
            name=str(request.POST.get('username','nil')).strip()
            password=str(request.POST.get('password','nil')).strip()
            email=request.POST.get('email','nil')
           
            if not name.isalnum():
                messages.error(request,"username must be alpha numeric!".title())
                return redirect('/userauth/registerpage')

            if len(name)>20:
                messages.error(request,'username must not be greater than 20 characters!'.title())
                return redirect('/userauth/registerpage')
            
            if len(password) < 5 :
                messages.error(request,'length of password is too short! must be greater than 5 characters'.title())
                return redirect('/userauth/registerpage')

            allusers=User.objects.all()
            isUserAlreadyPresent=False
            for currentuser in allusers:
                if currentuser.username==name:
                    isUserAlreadyPresent=True
            # a=database.objects.filter(username=name)
            if isUserAlreadyPresent:
                messages.error(request,"Sorry, a user with this username already exists. Try other username!")
                return redirect('/userauth/registerpage')


            myuser=User.objects.create_user(username=name,password=password,email=email)
           
            myuser.save()
            messages.success(request,f"congratulations! {name} successfully registered")
            user=authenticate(username=name,password=password)
            login(request,user)
            return redirect('/')

    else:
        return HttpResponse('404 page not found')
    
def logoutHandle(request):
        logout(request)
        messages.success(request,"successefully logged out")
        return redirect('/')

@csrf_exempt
def loginHandle(request):
    
        if request.method=='POST':
                username=request.POST['username']
                password=request.POST['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,f"{username} successfully logged in")
                    return redirect('/')
                else:
                    messages.error(request,"invalid credentials!! please try again")
                    return redirect('/userauth/login')
            
        else:
            return HttpResponse('404 page not found')