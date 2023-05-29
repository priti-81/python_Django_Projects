from django.shortcuts import render
import random

# Create your views here.
def index(request):
    data={'num':random.randint(1001,1999)}
    return render(request,'index.html',data)

def business(request):
    return render(request,'business.html')

def aboutus(request):
    return render (request,'aboutus.html')