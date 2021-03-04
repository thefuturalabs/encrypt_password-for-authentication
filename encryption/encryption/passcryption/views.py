from django.shortcuts import render,redirect
from .forms import UserCreateForm
from .shaencryption import shaencryption
from .decryption import decrypt_new,convert_password
from .otpmail import otpmail1
from .models import *
from .onetimeotp import *
import os,math
import random,sys
import smtplib
# Create your views here.
def index(request):
    return render(request, 'index.html')
def registration(request):
    return render(request, 'registration.html')
def signup(request):
  if request.method == 'POST':
    password1 = request.POST['password1']
    print(password1)
    password2=request.POST['password2']
    username=request.POST['username']
    email1=request.POST['email']
    if(password1==password2):
        print('matched')
        passs=shaencryption(password1)
        print('data',passs)
        user_login.objects.create(name=username,email=email1,password=passs,status=False)
        otp=otpmail1(email1)
        print(otp)
        print('created')
        OTP = mailsend(email1)
        return redirect('otpstat',OTP=OTP,uname=username)


    else:
        print('not matched')

  return render(request, 'registration.html')

def otpstat(request,OTP,uname):
    print('pass',OTP)

    print(uname)
    if request.method == 'POST':
        print('post')
        OTP1 = request.POST['otp']
        print('our',OTP1)
        if int(OTP1)==int(OTP):
            print('eql')
            data= user_login.objects.get(name=uname)
            data.status=True
            stat= data.status
            data.save()
            return  redirect('login_new')
        else:
            return redirect('otpstat',OTP=OTP,uname=uname)

    return render(request,'otp.html')



def de_login(request):
    if request.method == 'POST':
        password_new = request.POST['password']
        username1 = request.POST['username']
        g=user_login.objects.get(name=username1)
        old=g.password
        user=g.name

        if g.status:
            print(g.password)
            password_old=decrypt_new(old)
            pass_new=convert_password(password_new)

            if (password_old==pass_new):
                print("matched")
                message='username and password matched'
                return render(request, "index.html", {"messages":message})
            else:
                print("not matched")
                message='username and password not matched'
                return render(request, "index.html", {"messages":message})


    return render(request,'login.html')
