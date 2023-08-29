from django.shortcuts import render,redirect
from django.views import View
from .forms import SignupForm,CustomerProfileForm,SalerInfoForm,MyForm
from .models import CustomUser,UserSelection,SelectedAmenities
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
    form_A=MyForm()

    if request.method == 'POST':
        if request.POST.get('salerinfo') == 'salerinfo': 
            form = SalerInfoForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('sell_rent') 
                
        if 'info' in request.POST: 
            form_A = MyForm(request.POST)
            if form_A.is_valid() :
                saler_info = form_A.cleaned_data['Saler_InfoId']
                print(saler_info)
                selected_amenities = form_A.cleaned_data['select_amenities']
                print(selected_amenities)

            for amenity in selected_amenities:
                SelectedAmenities.objects.create(saler_info=saler_info, amenity=amenity)

          

            return redirect('sell_rent')
    return render(request, 'sell_rent.html', {'form': form,'form_A':form_A,})

