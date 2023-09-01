from django.shortcuts import render,redirect
from django.views import View
from .forms import SignupForm,CustomerProfileForm,SalerInfoForm
from .models import CustomUser,UserSelection,SalerInfo
from django.contrib import messages

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





# def login(request):
#     return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def bloggrid(request):
    return render(request,'blog-grid.html')

def buy(request,id):
    seller_data=SalerInfo.objects.get(id=id)
    selected_amenities=seller_data.amenities.all()
    return render(request,'buy.html',{'sellerdata':seller_data,'selectedamenities':selected_amenities})



# def sell_rent(request):
#     form = SalerInfoForm()
#     form_A=AmenitiesForm()
#     if request.method == 'POST':
#         if request.POST.get('salerinfo') == 'salerinfo': 
#             form = SalerInfoForm(request.POST,request.FILES)
#             if form.is_valid():
#                 form.save()
#                 contactdata=request.POST['Contactno']
#                 saler_infoid=SalerInfo.objects.get(Contactno=contactdata)
#                 print('ID:',saler_infoid.id)
#                 if saler_infoid:
#                     request.session['usercontact']=contactdata
#                     request.session['userid']=saler_infoid.id
#                 return redirect('sell_rent') 
                
#         if 'info' in request.POST: 
#             form_A = AmenitiesForm(request.POST) 
#             if form_A.is_valid() :
#                 print(form_A.cleaned_data,'---------------------')

#                 saler_info_id=request.session.get('userid') 
#                 try:
#                     saler_info= SalerInfo.objects.get(id=saler_info_id) 
#                     user_amenities = form_A.save(commit=False)
#                     user_amenities.Saler_InfoId = saler_info  # saler_info instance 
#                     user_amenities.save()
#                     form_A.save_m2m()  # Save when  many-to-many relationships created
#                     request.session.clear()
#                 except SalerInfo.DoesNotExist:
#                     print('This Salerid does not exist')

#                 return redirect('sell_rent')
#     return render(request, 'sell_rent.html', {'form': form,'form_A':form_A})



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

