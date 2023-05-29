from django.shortcuts import render,redirect
from .forms import userform
from .models import userinfo

# Create your views here.
def index(request):
    if request.method=='POST':
        newuser=userform(request.POST)
        print(newuser)
        if newuser.is_valid():
            newuser.save()
            print('your data submitted successfully..')
        else:
            print(newuser.errors)
    return render(request,'index.html',{'name':'priti'})

def Resources(request):
    return render(request,'Resources.html')

def Business(request):
    return render(request,'Business.html')

def showdata(request):
    data=userinfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
    update=userinfo.objects.get(id=id)
    if request.method=='POST':
        newuser=userform(request.POST,instance=update)
        if newuser.is_valid():
            newuser.save() 
            return redirect('showdata')
        else:
            print(newuser.errors)
    return render (request,'updatedata.html',{'cid':update})


def deletedata(request,id):
    delete=userinfo.objects.get(id=id)
    userinfo.delete(delete)
    return redirect ('showdata')



