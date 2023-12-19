from django import forms
from django.forms import widgets
from .models import Comment

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