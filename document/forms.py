#-*- coding: utf-8 -*-

from django.db import forms
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


from .models import *
from profiles.models import * 

class AddDocument(forms.ModelForm):
	name = forms.CharField(label=u"İsim", max_length=50, required=True)
    description = forms.CharField(label=u"Acıklama", max_length=1000, 
                                required=True, widget=forms.Textarea)