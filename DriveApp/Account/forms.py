from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm
from django.forms import widgets
import random

from Account.models import Profile
from Drive.models import Department, Scholl

class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control form-control-user", "placeholder":"E-Posta Adresi"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-control-user", "placeholder":"Şifre"}))
    remember_me = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={"class":"custom-control-input"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not User.objects.filter(email=email).exists():
            self.add_error("email","E-Mail ile kayıtlı bir kullanıcı bulunamadı.")

        return email

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Şifre"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Şifre(tekrar)"})
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Adı"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Soyadı"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control form-control-user","placeholder":"E-Posta Adresi"})
        self.fields["email"].required = True
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
    
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error("email","email daha önce kullanılmış")
        
        return email
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get("password1"))
        user.username = "{}_{}_{}".format(
            self.cleaned_data.get("first_name").replace("ğ","g").replace("ü","u").replace("ş","s").replace("ı","i").replace("ö","o").replace("ç","c").lower(),
            self.cleaned_data.get("last_name").replace("ğ","g").replace("ü","u").replace("ş","s").replace("ı","i").replace("ö","o").replace("ç","c").lower(),
            random.randint(1,99)
        )

        if commit:
            user.save()

        return user
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =("first_name","last_name","email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"First Name"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Soyadı"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control","placeholder":"E-Posta"})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =("avatar","date_of_birth","gender","scholl","department",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["avatar"].widget = widgets.FileInput(attrs={"class":"form-control","placeholder":"Avatar"})
        self.fields["date_of_birth"].widget = widgets.DateInput(attrs={"class":"form-control","placeholder":"Doğum Tarihi"})
        self.fields["gender"] = forms.ChoiceField(label="Cinsiyet",choices=Profile.genders, widget=forms.Select(attrs={'class': 'form-control'}))

        self.fields["scholl"] = forms.ModelChoiceField(
            queryset=Scholl.objects.all(),
            empty_label="Üniversite(Okul) Seçiniz",
            label="Üniversite(Okul)",
            widget=forms.Select(attrs={'class': 'form-control'})
            )
        
        self.fields["department"] = forms.ModelChoiceField(
            queryset=Department.objects.all(),
            empty_label="Bölüm Seçiniz",
            label="Bölüm",
            widget=forms.Select(attrs={'class': 'form-control'})
            )
        


