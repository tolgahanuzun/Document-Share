#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from django.core.files.base import ContentFile
from django.db.models import Q
from django.http import *

from department.models import Department
from document.models import Document
from profiles.models import Profile 

class AddDocument(forms.ModelForm):
    name = forms.CharField(label=u"İsim", max_length=50, required=True)
    description = forms.CharField(label=u"Acıklama", max_length=1000, 
                                required=True, widget=forms.Textarea)
    docfiles = forms.FileField(label=u"Upload Document", required=False)
    send_Department = forms.ModelChoiceField(label=u"departmen Name",
        queryset=Department.objects.all(), required=True)
    class Meta:
        model = Document
        fields = ("name", "description","docfiles","send_Department", "user")

    
    def save(self, commit=True):

        document = Document()
        document.name = self.data.get("name")
        document.description = self.data.get("description")

        send_Department = Department.objects.get(department_Name=
            self.data.get("department_Name"))
        document.send_Department = send_Department
        document.user = self.user
        document.save()
 
        return document    