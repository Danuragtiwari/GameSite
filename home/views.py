from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from __future__ import unicode_literals

# Create your views here.
def index(request):
   return render(request,'index.html')
def signup(request):
    pass
def login(request):
    pass
def logout(request):
    pass