from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*arg,**kwargs):
    return render(request, "home.html",{})
def page_error(request,*arg,**kwargs):
    return render(request, "error.html",{})