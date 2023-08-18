from .models import CustomUser
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
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),'email':forms.EmailInput(attrs={'class':'form-control'}),'contactno':forms.NumberInput(attrs={'class':'form-control'})}