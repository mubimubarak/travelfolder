from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Person
# Create your views here.


def demo(request):
    obj=Place.objects.all()
    guy=Person.objects.all()
    return render(request,"index.html",{"result":obj,"value":guy})
# def addition(request):
#     x= int(request.GET['num1'])
#     y =int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
