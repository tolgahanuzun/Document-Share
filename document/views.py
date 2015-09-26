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
from django.utils import timezone

def addDocumentViews(request):
    Depart = Department.objects.all()

    if request.user.is_authenticated():

        if request.method == "POST":
            form_addDocument = AddDocument(request.POST,request.FILES, user=request.user)
            dep_name = request.POST.get("send_Department") 
        
            if form_addDocument.is_valid():
               

                save_doc = form_addDocument.save()
                save_doc.send_Department.add(Department.objects.get(id=dep_name))
                save_doc.doc_file=request.FILES['doc_file']
                save_doc.save()
                
                 
                return HttpResponseRedirect("/")
            else:
                form_addDocument = AddDocument()
                return render(request,"add.html",
                                   locals())

        else:
            form_addDocument = AddDocument()
            return render(request, "add.html", {'form_addDocument':form_addDocument,"Depart":Depart})  

    else:
        return HttpResponseRedirect("/")

def documentAvailable(all_document):
    if all_document.count() == 0:
        return False

    return True        

def home(request):
    if request.user.is_authenticated():

        Depart = Department.objects.all()
        AllDocument = Document.objects.order_by("-createtime")
        Document_available = documentAvailable(AllDocument)
        currentTime = timezone.localtime(timezone.now())
        
        print Department.department_Members
        if request.user == Department.department_Members:
            print Depart

        return render(request, "index.html", 
                      {'AllDocument':AllDocument, 'currentTime':currentTime,
                       'Document_available':Document_available,'Depart':Depart})
    else:
        return render(request, "index.html")