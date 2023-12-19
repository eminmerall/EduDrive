from django.shortcuts import render

# Create your views here.

def login_request(request):
    return render(request, 'Account/login.html')

def register_request(request):
    return render(request, 'Account/register.html')

def change_password(request):
    return render(request, 'Account/change_password.html')

def logout_request(request):
    pass
