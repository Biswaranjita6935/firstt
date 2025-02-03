from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Chuin(request):
    return HttpResponse('Chuin is a worst girl')
def Biswa(request):
    return HttpResponse('<h1> My Name is Biswa...</h1>')