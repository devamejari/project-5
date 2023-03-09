from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def dhoni(request):
    return HttpResponse('<h1> this is dhoni</h1>')

def mahindra(request):
    return HttpResponse('<h1> this is mahindra</h1>')

def deva(request):
    return HttpResponse('<h1> this is deva</h1>')

def mahi(request):
    return HttpResponse('<h1> this is mahi</h1>')