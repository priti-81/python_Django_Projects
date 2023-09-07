from django.shortcuts import render,redirect
from django.views import View
from .forms import SignupForm,CustomerProfileForm,SalerInfoForm,ContactForm
from .models import CustomUser,UserSelection,SalerInfo
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    saler_infodata=SalerInfo.objects.all()
    return render(request,'index.html',{'salerdata':saler_infodata})


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


def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
           
            html=render_to_string('contact/email.html',
                                  {'name':name,
                                  'email':email,
                                  'subject':subject,
                                  'message':message})
    
            send_mail('ContactForm','This is message','priti@gmail.com',['djangotest2023@gmail.com'],html_message=html)
            messages.success(request,'Your Message has been sent successfully!! Thank u')
            return redirect('contact')
    else:
        form=ContactForm()
    return render(request,'contact.html',{'form':form})


def bloggrid(request):
    return render(request,'blog-grid.html')

def propertygrid(request):
    saler_infodata=SalerInfo.objects.all()
    return render(request,'property-grid.html',{'salerdata':saler_infodata})


@login_required
def buy(request,id):
    seller_data=SalerInfo.objects.get(id=id)
    selected_amenities=seller_data.amenities.all()
    return render(request,'buy.html',{'sellerdata':seller_data,'selectedamenities':selected_amenities})



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


@login_required
def sell_rent(request):
    form = SalerInfoForm()

    if request.method == 'POST':
        if request.POST.get('salerinfo') == 'salerinfo': 
            form = SalerInfoForm(request.POST,request.FILES)
            if form.is_valid():
                saler_info = form.save(commit=False)
                print(saler_info)  # Create an instance but don't save yet
                saler_info.save()  # Save the instance to the database
                form.save_m2m()  # Save the many-to-many relationships (selected amenities)
                messages.success(request,'Congratulations!! Your form submited Successfully')
                return redirect('sell_rent') 
    return render(request, 'sell_rent.html', {'form': form})

