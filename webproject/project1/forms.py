from django import forms
from .models import signupinfo

class userform(forms.ModelForm):
    class Meta:
        model=signupinfo
        fields='__all__'