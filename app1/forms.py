from django import forms
from .models import Student
from django.core import validators

class student_registration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }

# class student_registration(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))