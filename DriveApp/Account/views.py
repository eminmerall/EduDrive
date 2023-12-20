from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from Account.forms import LoginForm


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
    return render(request, 'Account/register.html')

def change_password(request):
    return render(request, 'Account/change_password.html')

def logout_request(request):
    pass
