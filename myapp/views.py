from django.shortcuts import render,redirect
from myapp.models import user_data
from django.contrib import messages
# Create your views here.

def sign_view(request):
    if request.method=="POST":
        name=request.POST.get('username')
        print(name)
        mail=request.POST.get('email')
        pas=request.POST.get('password')
        user_data.objects.create(user_name=name,email=mail,password=pas)
    context={
        'word1':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Debitis,ex ratione. Aliquid!',
        'word2':'subham'
    }

    return render(request,'log.html',context)


def sign_in(request):
    if request.method=='POST':
        name=request.POST.get('name_login')
        pas=request.POST.get('p_word')
        print(name)
        print(pas)
        user=user_data.objects.filter(user_name=name,password=pas)
        print(user)
        if user.exists():
            request.session['user']=name
            return redirect('/')
        else:
            messages.error(request,"data didn't exist!")
    return render(request,'log.html',)


def index_view(request):
    return render(request,'index.html')