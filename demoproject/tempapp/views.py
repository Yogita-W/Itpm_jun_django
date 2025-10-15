from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def basePage(request):
    return render(request,'basePage.html')
def childPage(request):
    return render(request,'childPage.html')
def childPage2(request):
    return render(request ,'childPage2.html')
def header(request):
    return render(request,'header.html')
