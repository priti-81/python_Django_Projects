from django.shortcuts import render,redirect
from .forms import noteForm,updateForm,noteSubmitForm
from .models import noteSignup
from django.core.mail import send_mail
from notepro1 import settings
from random import randint
from django.contrib.auth import logout


# Create your views here.
def index(request):
    if request.method == "POST":
        if request.POST.get("signup")=="signup":
            newuser=noteForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("data saved successfully")
                eml=request.POST['email']
                print(eml)
                # sending email
                otp=randint(111111,999999)
                sub="congrats"
                msg=f" Welcome user\n you successfully signin our website....\n your otp is {otp} \n if you have any query feel free to contact +778888898456"
                from_email=settings.EMAIL_HOST_USER
                to_mail=[eml]

                send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_mail)

            else:
                print(newuser.errors)

        elif request.POST.get('login')=='login':
            unm=request.POST['email']

            userid=noteSignup.objects.get(email=unm)
            print(userid)
            print('ID:',userid.id)
            
        
            if userid: #true
                print('login successfully')
                request.session['username']=unm #create a session
                request.session['userid']=userid.id
                return redirect('note')
            else:
                print("Error! Login failed....")     
    user=request.session.get('username')
    return render(request,'index.html',{'username':user})

def aboutus(request):
    user=request.session.get('username')
    return render(request,'aboutus.html',{'username':user})


def contactus(request):
    user=request.session.get('username')
    return render(request,'contactus.html',{'username':user})

def notes(request):
    user=request.session.get('username')
    if request.method=='POST':
        form=noteSubmitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('note submited successfully')
        else:
            print(form.errors)
    return render(request,'notes.html',{'userdata':user,'username':user})


def profile(request):
    user=request.session.get('username')
    return render(request,'profile.html',{'username':user})

def update(request):
    userid=request.session.get('userid')
    cuser=noteSignup.objects.get(id=userid)
    print(cuser)
    if request.method=='POST':
        updateuser=updateForm(request.POST,instance=cuser)
        if updateuser.is_valid():
            updateuser.save()
            return redirect('note')
        else:
            print(updateuser.errors)

    return render(request,'update.html',{'cid':cuser})

def delete(request):
    userid=request.session.get('userid')
    deleteuser=noteSignup.objects.get(id=userid)
    noteSignup.delete(deleteuser)
    return redirect('/')

def userlogout(request):
    logout(request)
    return redirect ('/')