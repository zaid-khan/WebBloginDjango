from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<b>This is the home page.</b>")
# Create your views here.
