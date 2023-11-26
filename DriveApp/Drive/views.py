from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def files(request):
    return render(request,'files.html')

def files_details(request, slug):
    return render(request,'file-details.html',{
        "slug":slug
    })
