from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')


def contactus(request):
    return render(request,'contactus.html')

def notes(request):
    return render(request,'notes.html')


def profile(request):
    return render(request,'profile.html')


