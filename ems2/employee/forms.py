from dataclasses import fields
from django.forms import ModelForm, forms, models, widgets,TextInput,Textarea
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['empId','first_name','last_name','city','address','dob','mobile']
        widgets = {
            
            'address': Textarea(attrs={'cols': 70, 'rows': 3}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Email already exist')
        return email