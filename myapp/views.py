from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request,'log.html',{})

def index_view(request):
    return render(request,'index.html')