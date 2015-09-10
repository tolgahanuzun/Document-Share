#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.files.base import ContentFile
from django.db.models import Q
from django.http import *

from department.models import Department
from profiles.models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if not username or not password:
            return self.cleaned_data

        user = authenticate(username=username,
                            password=password)

        if user:
            self.user = user
        else:
            raise ValidationError("Yanlış kullanıcı adı veya şifre!")

        return self.cleaned_data    


class RegistrationForm(UserCreationForm):
    department_name = forms.ModelChoiceField(label=u"departmen Name",
        queryset=Department.objects.all(), required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "department_name", "password1", "password2")
     
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)


        if commit:
            user.backend='django.contrib.auth.backends.ModelBackend'
            user.save()
            user_profile = Profile()
            user_profile.user = user
            user_profile.save()


            department = Department.objects.get(department_Name=self.cleaned_data['department_name'])
            department.department_Members.add(user)
        
        return user


        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        
