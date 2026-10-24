from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def displayHello(request):
    return HttpResponse("Hello, world. You are at the hello app !!!")