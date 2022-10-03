from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def welcome (request):
    return render(request,'welcome.html')
def enrol(request):
    return render(request,"form.html")
def form (request):
    if request.method == 'POST':
        name = request.POST['name']
        dob= request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone number']
        email = request.POST['email']
        address = request.POST['address']
        user=auth.authenticate(name=name,dob=dob,age=age,gender=gender,phone=phone,email=email,address=address)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credential")
            return redirect('credentials:mypage')

    return render(request,"form.html")
def logout (request):
    auth.logout(request)
    return redirect('/')

def mypage (request):
    return render(request,"mypage.html")

def fun (request):
    return redirect('/')



def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('credentials:welcome')
        else:
            messages.info(request,"invalid credential")
            return redirect('credentials:welcome')
    return render(request,'login.html')

def register(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username Already Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)

                user.save();
                return redirect('credentials:login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')