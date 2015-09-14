#-*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import *
from django.template import Template, Context, RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from department.models import Department
from document.models import Document
from document.forms import AddDocument

def addDocumentViews(request):
    Depart = Department.objects.all()
    if request.user.is_authenticated():
        if request.method == "POST":
            form_addDocument = AddDocument(request.POST, user=request.user)
            if form_addDocument.is_valid():
                form_addDocument = form_addDocument.save()
                AddDocument.save() 
                return HttpResponseRedirect("/")
        else:
            form_addDocument = AddDocument()
            return render(request, "add.html", {'form_addDocument':form_addDocument,"Depart":Depart})  
    else:
        return HttpResponseRedirect("/")

