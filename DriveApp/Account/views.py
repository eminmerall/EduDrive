from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from Account.forms import CreateUserForm, LoginForm, ProfileForm, UserForm, UserPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home_page")
    
    if request.method == "POST":

        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            remember_me = form.cleaned_data.get("remember_me")
            
            if User.objects.filter(email=email).exists():
                username = User.objects.get(email=email).username
                user = authenticate(username=username, password=password)
                if user is not None:
                    if not remember_me:
                        request.session.set_expiry(0)
                        request.session.modified=True
                        
                    login(request, user)
                    return redirect("home_page")
                
                else:
                    form.add_error(None, "Kullanıcı bilgilerini hatalı girdiniz. Lütfen tekrar deneyin")
                    return render(request, 'Account/login.html',{'form':form})
            
        else:
            return render(request, 'Account/login.html',{'form':form})


    form = LoginForm()
    return render(request, 'Account/login.html',{'form':form})

def register_request(request):
    if request.user.is_authenticated:
        return redirect("home_page")
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            print(user.username)
            username = user.username
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password = password)
            login(request, user)
            return redirect("home_page")
        else:
            form.add_error(None, "Lütfen tüm alanları doldurun!")
            return render(request, 'Account/register.html',{'form':form})      

    form = CreateUserForm()
    return render(request, 'Account/register.html',{'form':form})

def change_password(request):
    form= UserPasswordChangeForm(request.user)
    if request.method=="POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,"Parola Değiştirildi")
            return redirect("change_password")
        else:
            return render(request, 'Account/change-password.html',{"form":form})
            
    return render(request, 'Account/change-password.html',{"form":form})

@login_required(login_url='/Account/login')
def profile(request):
    if request.method =="POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, istance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Profil bilgileriniz güncellendi.")
            return redirect("profile")
        else:
            messages.error(request,"Lütfen bilgilerinizi kontrol ediniz")
    else:        
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'Account/profile.html',{
        'user_form':user_form,
        'profile_form':profile_form
    })

def liked_files(request):
    return render(request, 'Account/liked-files.html')

def logout_request(request):
    logout(request)
    return redirect("home_page")
