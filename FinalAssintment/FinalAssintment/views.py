
 
from django.shortcuts import render
from django.http import HttpResponse

def helloview(request):
    return HttpResponse("helloWorld")
