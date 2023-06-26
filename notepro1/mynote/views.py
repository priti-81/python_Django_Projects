from django.shortcuts import render,redirect
from .forms import noteForm,updateForm,noteSubmitForm
from .models import noteSignup


# Create your views here.
def index(request):
    if request.method == "POST":
        if request.POST.get("signup")=="signup":
            newuser=noteForm(request.POST)
            print(newuser)
            if newuser.is_valid():
                newuser.save()
                print("data saved successfully")
            else:
                print(newuser.errors)

        elif request.POST.get('login')=='login':
            unm=request.POST['email']
            pas=request.POST['password']

            userid=noteSignup.objects.get(email=unm)
            print(userid)
            print('ID:',userid.id)
            
        
            if userid: #true
                print('login successfully')
                request.session['user']=unm #create a session
                request.session['userid']=userid.id
                request.session['username']=userid.name
                return redirect('note')
            else:
                print("Error! Login failed....")
                

    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')


def contactus(request):
    return render(request,'contactus.html')

def notes(request):
    user=request.session.get('user')
    uname=request.session.get('username')
    if request.method=='POST':
        form=noteSubmitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('note submited successfully')
        else:
            print(form.errors)
    return render(request,'notes.html',{'user':user,'uname':uname})


def profile(request):
    return render(request,'profile.html')

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
