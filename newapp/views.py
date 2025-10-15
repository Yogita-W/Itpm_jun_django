from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request ,'home.html',{'name':'Yogita'})

def login(request):
    return render(request,'login.html')

def home1(request):
    return render(request,'home1.html')
 
def feedback(request):
    return render(request,'feedback.html',{'name':'Yogita'})  