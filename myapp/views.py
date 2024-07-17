from django.shortcuts import render,redirect
from myapp.models import user_data
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_view(request):
    if request.method=="POST":
        name=request.POST.get('username')
        mail=request.POST.get('email')
        pas=request.POST.get('password')
        if name and mail and pas:
            user= User.objects.create(
                username = name,
                email=mail,
                password=pas
            )
            user.set_password(pas)
            user.save()
            messages.info(request,'account created successfully')
            return redirect('sign_in/')
        else:
            messages.error(request,'Provide valid detail')
    else:
        messages.error(request,'Provide valid request')
        
    return render(request,'log.html')

    


def sign_in(request):
    if request.method=='POST':
        name=request.POST.get('name_login')
        pas=request.POST.get('p_word')

        user = authenticate(username=name,password=pas)
        if user.exists():
            login(request,user)

          
        else:
            messages.error(request,"data didn't exist!")
    return render(request,'log.html',)


def index_view(request):
    return render(request,'index.html')