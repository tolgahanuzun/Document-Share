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
    # name = forms.CharField(label=u"İsim", max_length=50, required=True)
    # description = forms.CharField(label=u"Acıklama", max_length=1000, 
    #                             required=True, widget=forms.Textarea)
    doc_file = forms.FileField(label=u"Upload Document", required=False)
    #send_department = forms.ModelChoiceField(label=u"departmen Name",
    #   queryset=Department.objects.all(), required=True)

    class Meta:
        model = Document
        fields = ("name","description","doc_file","send_Department")

# Hatalı kısım
    
    def save(self, commit=True):
        savedoc = Document()

        savedoc.name = self.data.get("name")
        print savedoc.name
        savedoc.description = self.data.get("description")
        print savedoc.description
        senddepart = Department.objects.get(department_Name=self.data.get("send_Department"))
        print senddepart
        savedoc.send_Department = senddepart
        print savedoc.send_Department

        savedoc.doc_file = self.data.get("doc_file")

        savedoc.save()
        return savedoc    
# Hatalı kısım