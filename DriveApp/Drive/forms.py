from django import forms
from django.forms import widgets
from Account.models import Profile
from Drive.models import Department, Scholl ,Lesson, Comment, File, Outhor
from PIL import Image
import random
import uuid


class SchollForm(forms.ModelForm):
    class Meta:
        model = Scholl
        fields = ['name', 'contact']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Üniversite(Okul) Adı"})



class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name','scholl']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Ders Adı"})
        self.fields["scholl"] = forms.ModelChoiceField(
            queryset=Scholl.objects.all(),
            empty_label="Üniversite(Okul) Seçiniz",
            label="Üniversite(Okul)",
            widget=forms.Select(attrs={'class': 'form-control'})
            ) 
    

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name', 'department']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Ders Adı"})
        self.fields["department"] = forms.ModelChoiceField(
            queryset=Department.objects.all(),
            empty_label="Bölüm Seçiniz",
            label="Bölüm",
            widget=forms.Select(attrs={'class': 'form-control'})
            )  
        
class OuthorForm(forms.ModelForm):
    class Meta:
        model = Outhor
        fields = ['first_name', 'last_name', 'biography', 'image_name', 'date_of_birth', 'gender', 'title_type', 'contact']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Adı"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Soyadı"})
        self.fields["biography"].widget = widgets.Textarea(attrs={"class":"form-control","rows":"4","placeholder":"Özgeçmiş"})
        self.fields["image_name"].widget = widgets.FileInput(attrs={"class":"form-control","placeholder":"Profil Resmi"})
        self.fields["date_of_birth"].widget = widgets.DateInput(attrs={"class":"form-control","placeholder":"Doğum Tarihi"})
        self.fields["gender"] = forms.ChoiceField(label="Cinsiyet",choices=Outhor.genders, widget=forms.Select(attrs={'class': 'form-control'}))
        self.fields["title_type"] = forms.ChoiceField(label="Unvan",choices=Outhor.title_tpyes, widget=forms.Select(attrs={'class': 'form-control'}))


class CommentForm(forms.ModelForm):
    class Meta:
        numbers = (
            ('1', '1 Yıldız'),
            ('2', '2 Yıldız'),
            ('3', '3 Yıldız'),
            ('4', '4 Yıldız'),
            ('5', '5 Yıldız'),
        )
        model = Comment
        # fields = ['usename','email','text','rating']
        exclude = ['file','date_added']
        labels = {
            "username":"Kullanıcı Adı",
            "email":"E-Posta Adresi",
            "text":"Yorum",
            "rating":"Puan"
        }
        widgets = {
            "username": widgets.TextInput(attrs={"class":"form-control"}),
            "email": widgets.EmailInput(attrs={"class":"form-control"}),
            "text": widgets.Textarea(attrs={"class":"form-control"}),
            "rating": widgets.Select(attrs={"class":"form-control custom-select"}, choices=numbers),
        }



class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['title','file_name','description', 'language', 'outhor', 'scholl', 'department', 'lesson','file_cover']

    def clean(self):
        cleaned_data = super().clean()
        file_name = cleaned_data.get('file_name')

        if file_name:
            file_extension = file_name.name.split('.')[-1].lower()
            if file_extension not in ['jpg', 'jpeg', 'png', 'gif','txt','xlsx','xls','doc','docx','txt','pdf']:
                self.add_error('file_cover',"Lütfen geçerli bir dosya yükleyin yükleyin. İzin verilen dosya türleri: jpg, png, gif, txt, xlsx,doc, docx,txt,pdf ")
            else:
                if file_extension in ['doc', 'docx', 'txt']:
                    cleaned_data['file_cover'] = 'icons/word.png'
                if file_extension in ['xls', 'xlsx']:
                    cleaned_data['file_cover'] = 'icons/excel.png'
                if file_extension in ['pdf']:
                    cleaned_data['file_cover'] = 'icons/pdf.png'
                if file_extension in ['jpg','jpeg','png','gif']:
                    cleaned_data['file_cover'] = 'icons/image.png'

        return cleaned_data
    exclude = ['file_cover']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields["title"].widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Dosya Başlığı"})
        self.fields["file_name"].widget = widgets.FileInput(attrs={"class":"form-control","placeholder":"Dosya"})
        self.fields["description"].widget = widgets.Textarea(attrs={"class":"form-control","rows":"4","placeholder":"Okul"})
        self.fields["language"].widget = forms.Select(choices=File.languages, attrs={'class': 'form-control',"placeholder":"Dil"})
        self.fields['file_cover'].widget = forms.HiddenInput()
        self.fields['file_cover'].required = False

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
        
        self.fields["lesson"] = forms.ModelChoiceField(
            queryset=Lesson.objects.all(),
            empty_label="Ders Seçiniz",
            label="Ders",
            widget=forms.Select(attrs={'class': 'form-control'})
            )

        self.fields["outhor"] = forms.ModelChoiceField(
            queryset=Outhor.objects.all(),
            empty_label="Yazar Seçiniz",
            label="Yazar",
            widget=forms.Select(attrs={'class': 'form-control'})
            ) 
        

           
    