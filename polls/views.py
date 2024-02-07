from django.shortcuts import render

from django.http import HttpResponse 

def index (request):
    return HttpResponse("starting from here")
# Create your views here.
