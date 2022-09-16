from email.policy import HTTP
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def now(request):
    return HttpResponse("Hello")

def first(request):
    return HttpResponse('My first hit')

def second(request):
    return HttpResponse('My second hit')

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html') 

def login(request):
    data=request.POST
    username=data.get("username")
    password=data.get("password")
    print(password)  
    print(username)     
    return render(request , 'index.html')

   