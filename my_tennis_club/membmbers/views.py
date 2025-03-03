from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello SF231 world!")