from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from Drive.forms import CommentForm, FileUploadForm, FileEditForm, SchollForm, DepartmentForm, LessonForm, OuthorForm
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from Drive.models import File, Slider, Scholl, Department, Lesson, Outhor
from Account.models import Profile
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/Account/login')
def index(request):
    files = File.objects.filter(is_active=True, is_home=True) 
    sliders= Slider.objects.filter(is_active=True)
    return render(request, 'Drive/index.html',{
        "files": files,
        "sliders":sliders
    })

@login_required(login_url='/Account/login')
def files(request):
    files = File.objects.filter(is_active=True) 
    return render(request,'Drive/files.html',{
        "files": files
    })

@login_required(login_url='/Account/login')
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

@login_required(login_url='/Account/login')
def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.date = timezone.now()
            file_instance.user = request.user
            file_instance.save()
            messages.success(request,"Dosya Yüklendi")
            return redirect('file_upload')
        else:
            print(form.errors)
    else:
        form = FileUploadForm()


    return render(request, 'Drive/file-upload.html', {'form': form})

@login_required(login_url='/Account/login')
def download_file(request, file_slug):
    file_obj = get_object_or_404(File, slug=file_slug)
    file_data = file_obj.file_name.read()
    response = HttpResponse(file_data, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file_obj.file_name.name}"'

    return response

@login_required(login_url='/Account/login')
def user_files(request):
    user_files = File.objects.filter(user=request.user)
    return render(request, 'Drive/user-files.html',{'user_files':user_files})

@login_required(login_url='/Account/login')
def edit_file(request, file_slug):
    file_instance = get_object_or_404(File, slug=file_slug)
    
    if request.method == 'POST':
        form = FileEditForm(request.POST, instance=file_instance)
        if form.is_valid():
            form.save()
            # Başarılı bir şekilde kaydedildiğinde yapılacak işlemler
    else:
        form = FileEditForm(instance=file_instance)
    
    return render(request, 'Drive/edit-file.html', {'form': form})

@login_required(login_url='/Account/login')
def add_school(request):
    if request.method == 'POST':
        form = SchollForm(request.POST)
        if form.is_valid():
            form.save()
            # Başarılı ekleme mesajı, başka bir sayfaya yönlendirme vs. burada yapılabilir.
    else:
        form = SchollForm()

    return render(request, 'Drive/addForms/add-school.html', {'form': form})

@login_required(login_url='/Account/login')
def scholl_list(request):
    scholls = Scholl.objects.all()
    return render(request, 'Drive/scholl-list.html', {'scholls': scholls})

@login_required(login_url='/Account/login')
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            # Başarılı ekleme mesajı, başka bir sayfaya yönlendirme vs. burada yapılabilir.
    else:
        form = DepartmentForm()

    return render(request, 'Drive/addForms/add-department.html', {'form': form})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'Drive/department-list.html', {'departments': departments})

@login_required(login_url='/Account/login')
def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            # Başarılı ekleme mesajı, başka bir sayfaya yönlendirme vs. burada yapılabilir.
    else:
        form = LessonForm()
    return render(request, 'Drive/addForms/add-lesson.html', {'form': form})

@login_required(login_url='/Account/login')
def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'Drive/lesson-list.html', {'lessons': lessons})

@login_required(login_url='/Account/login')
def add_outhor(request):
    if request.method=='POST':
        form = OuthorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OuthorForm()
    return render(request, 'Drive/addForms/add-outhor.html',{'form':form})

@login_required(login_url='/Account/login')
def outhor_list(request):
    outhors = Outhor.objects.all()
    return render(request, 'Drive/outhor-list.html', {'outhors': outhors})

@login_required(login_url='/Account/login')
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'Drive/profile-list.html', {'profiles': profiles})