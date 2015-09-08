# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.core.exceptions import ValidationError
from profiles.models import Profile
from department.models import Department
from profiles.forms import LoginForm, RegistrationForm
from django.http import *
from django.contrib.auth.forms import UserCreationForm

def index(request):
    context = {}
    populateContext(request, context)
    return render(request, 'index.html', context)

def login(request):
    context = {}
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
            else:
                context['error'] = 'Non active user'
        else:
            context['error'] = 'Wrong username or password'
    except:
        context['error'] = ''
    
    populateContext(request, context)
    return render(request, 'login.html', context)


def logout(request):
    context = {}
    try:
        auth_logout(request)
    except:
        context['error'] = 'Some error occured.'
    
    populateContext(request, context)
    return render(request, 'login.html', context)

def populateContext(request, context):
    context['authenticated'] = request.user.is_authenticated()
    if context['authenticated'] == True:
        context['username'] = request.user.username


    #Kayıt formu
def register(request): 
    Depart = Department.objects.all()
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if  form.is_valid():
            form.save()       
            return render(request,"register.html",
                               locals())
        else:

            form = RegistrationForm()
            return render(request,"register.html",
                               locals())
    else:
        form = RegistrationForm()
        return render(request, "register.html",
                    { 'form':form, "Depart":Depart})


# def register(request): 
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             kullanici = authenticate(username=form.cleaned_data['username'],
#                                      password=form.cleaned_data['password1'])
#             if kullanici.is_authenticated():
#                 login(request,kullanici)
#             return HttpResponseRedirect("/admin/")
#     else:
#         form = UserCreationForm()
#     return render_to_response("register.html",
#                               locals(),
#                               context_instance = RequestContext(request))