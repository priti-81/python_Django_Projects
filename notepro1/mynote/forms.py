from django import forms
from .models import noteSignup,myModel

class noteForm(forms.ModelForm):
    class Meta:
        model=noteSignup
        fields="__all__"

class updateForm(forms.ModelForm):
    class Meta:
        model=noteSignup
        fields="__all__"

class noteSubmitForm(forms.ModelForm):
    class Meta:
        model=myModel
        fields="__all__"