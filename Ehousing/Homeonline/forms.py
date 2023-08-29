from .models import CustomUser,SalerInfo
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation


class SignupForm(UserCreationForm):
    contactno = forms.IntegerField(min_value=0,error_messages={'required' :'Please enter your contact number'},widget=forms.NumberInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required' :'Please enter your password'})

    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required' :'Please enter your password again'})

    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}),error_messages={'required' :'Please enter your correct email'})

    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required' :'Please enter your username'})
    class Meta:
        model = CustomUser
        fields = ['username','contactno','email','password1','password2']
        labels = {'email': 'Email','contactno':'ContactNO'}

    def clean_contactno(self):
        contactno = self.cleaned_data.get('contactno')
        if len(str(contactno))>10:
            raise forms.ValidationError("Enter 10 digit ContactNo.")
        return contactno


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}),error_messages={'required' :'Please enter your username'})
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}),error_messages={'required' :'Please enter valid password'})

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"),strip=False,widget=forms.PasswordInput(
     attrs={"autocomplete": "current-password", "autofocus": True,'class':'form-control'}))

    new_password1 = forms.CharField(label=_("New password"),widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}),strip=False,help_text=password_validation.password_validators_help_text_html())
     
    new_password2 = forms.CharField(label=_("New password confirmation"),strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
     email = forms.EmailField(label=_("Email"),max_length=254,widget=forms.EmailInput(attrs={"autocomplete": "email",'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New password"),widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":'form-control'}),strip=False,help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("New password confirmation"),strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password",'class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','email','contactno']
        labels = {'email': 'Email','contactno':'ContactNO'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}),'contactno':forms.NumberInput(attrs={'class':'form-control'} )}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("This field is required.")
        return email
    

class SalerInfoForm(forms.ModelForm):
    class Meta:
        model=SalerInfo
        fields=['HouseOwnerName','Area','Contactno','BHK','Status','Upload_Image','House_Description','House_address','House_price','video_file']
        labels={'HouseOwnerName':'House Owner Name','Upload_Image':'Upload Image','House_Description':'House Description','House_address':'House Address','House_price':'House Price','video_file':'Upload video'}
        widgets={'HouseOwnerName':forms.TextInput(attrs={'class':'form-control'}),
        'Area':forms.NumberInput(attrs={'class':'form-control'}),
        'Contactno':forms.NumberInput(attrs={'class':'form-control'}),
        'BHK':forms.NumberInput(attrs={'class':'form-control'}),
        'Status':forms.Select(attrs={'class':'form-control'},choices=SalerInfo.status),
        'Upload_Image':forms.ClearableFileInput(attrs={'class':'form-control',}),
        'House_Description':forms.Textarea(attrs={'class':'form-control','rows': 5, 'cols': 5}),
        'House_address':forms.Textarea(attrs={'class':'form-control','rows': 5, 'cols': 5}),
        'House_price':forms.TextInput(attrs={'class':'form-control'}),
        'video_file':forms.FileInput(attrs={'class': 'form-control'})
        }



from django import forms
from .models import SalerInfo, UserSelection

class MyForm(forms.Form):
    Saler_InfoId = forms.ModelChoiceField(queryset=SalerInfo.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select'}))
    select_amenities = forms.ModelMultipleChoiceField(queryset=UserSelection.objects.all(), widget=forms.CheckboxSelectMultiple)


