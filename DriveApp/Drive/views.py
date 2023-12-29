from datetime import date
from django.shortcuts import render, get_object_or_404
from Drive.forms import CommentForm
from django.http.response import HttpResponseRedirect
from Drive.models import File, Slider
from django.urls import reverse




# Create your views here.
def index(request):
    files = File.objects.filter(is_active=True, is_home=True) 
    sliders= Slider.objects.filter(is_active=True)
    return render(request, 'Drive/index.html',{
        "files": files,
        "sliders":sliders
    })

def files(request):
    files = File.objects.filter(is_active=True) 
    return render(request,'Drive/files.html',{
        "files": files
    })

def file_details(request, slug):

    file = get_object_or_404(File, slug=slug)
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.file = file
            comment.save()
            return HttpResponseRedirect(reverse("file_details", args=[slug]))

    return render(request,'Drive/file-details.html',{
        "file": file,
        "comments":file.comments.all().order_by("-date_added"),
        "comment_form": comment_form
    })
