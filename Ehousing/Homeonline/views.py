from django.shortcuts import render,redirect
from django.views import View
from .forms import SignupForm,CustomerProfileForm
from .models import CustomUser
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')


class signupview(View):
    def get (self,request):
        form=SignupForm()
        return render (request,'signup.html',{'form':form})
    
    def post (self,request):
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render (request,'signup.html',{'form': form})





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

def updatedata(request):
    update=CustomUser.objects.get(id=request.user.id)
    if request.method=='POST':
        form=CustomerProfileForm(request.POST,instance=update)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations!! Profile Updated Successfully')
            return redirect('login')
        return render(request,'update.html',{'form':form})
    else:
        form=CustomerProfileForm()
        return render(request,'update.html',{'form':form})

def rent(request):
    return render(request,'rent.html')