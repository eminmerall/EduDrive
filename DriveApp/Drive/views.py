from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("index")

def files(request):
    return HttpResponse("files")

def files_details(request, slug):
    return HttpResponse("file_details:"+ slug)
