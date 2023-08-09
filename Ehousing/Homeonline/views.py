from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def bloggrid(request):
    return render(request,'blog-grid.html')

def buy(request):
    return render(request,'buy.html')

def sell(request):
    return render(request,'sell.html')

def update(request):
    return render(request,'update.html')

def rent(request):
    return render(request,'rent.html')