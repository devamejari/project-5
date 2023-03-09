from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
   return HttpResponse ('<h1><marquee> this is virat</h1></marquee>')

def raina(request):
   return HttpResponse('</h2><marquee>this is raina</h2></marquee>')