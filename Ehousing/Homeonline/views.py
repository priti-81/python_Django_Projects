from django.shortcuts import render,redirect
from django.views import View
from .forms import SignupForm,CustomerProfileForm,SalerInfoForm,AmenitiesForm
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



def sell_rent(request):
    form = SalerInfoForm()
    form_A = AmenitiesForm()
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('salerinfo') == 'salerinfo': 
            form = SalerInfoForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('sell_rent')     
        if request.POST.get('info') == 'info': 
            print('yes')
            form_A = AmenitiesForm(request.POST,request.FILES)
            if form_A.is_valid():
                print(form_A.cleaned_data)
                form_A.save()  
                return redirect('sell_rent')
            else:
               print(form_A.errors)

    return render(request, 'sell_rent.html', {'form': form, 'form_A': form_A})



def updatedata(request):
    update=CustomUser.objects.get(id=request.user.id)
    if request.method=='POST':
        form=CustomerProfileForm(request.POST,instance=update)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations!! Profile Updated Successfully, Please,Login again')
            return redirect('updateprofile')
        return render(request,'update.html',{'form':form})
    else:
        form=CustomerProfileForm(instance=update)
        return render(request,'update.html',{'form':form})

