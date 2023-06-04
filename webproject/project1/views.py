from django.shortcuts import render,redirect
from .forms import userform
from .models import signupinfo
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render (request,'index.html')

def login(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']
        user=signupinfo.objects.filter(username=unm,password=pas)
        print(user)
        if user:
            print('login successfully')
            request.session['user']=unm #create session ,user is a key name
            return redirect('mypage')
        else:
            messages.info(request, 'Hey, Newuser signup first...')

    return render (request,'login.html')
 
def signup(request):
    # print(request.method)
    if request.method=='POST':
        user=userform(request.POST)
        #print(user)
        if user.is_valid():
            user.save()
            messages.success(request, 'Congrates, you successfully signup..')
            return redirect('/login')
        else:
           print( user.errors)
           return render (request,'signup.html')
    else:
        return render (request,'signup.html')

def mypage(request):
    data=request.session.get('user')
    return render (request,'mypage.html',{'data':data})

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def password(request):
    return render(request,'password.html')

   
def userlogout(request):
    logout(request)
    return redirect('/')





