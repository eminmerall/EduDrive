from django.contrib.auth.models import User
from django.db import models
from django.core import validators
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.db.models.fields import CharField
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    adress = models.CharField("Adres", max_length=400)
    email = models.EmailField("E-Posta", null=True, blank=True)
    phone1 = models.CharField("Telefon 1", max_length=20,null=True, blank=True)
    phone2 = models.CharField("Telefon 2", max_length=20,null=True, blank=True)

    class Meta:
        verbose_name = "İletişim"
        verbose_name_plural = "İletişimler"

    def __str__(self):
        return self.email

class Scholl(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Okul(Üniversite) Adı", max_length=100)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Okul"
        verbose_name_plural = "Okullar"
    
    def __str__(self):
        return self.name

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Bölüm(Departman) Adı", max_length=100)
    scholl = models.ManyToManyField(Scholl)

    class Meta:
        verbose_name = "Bölüm"
        verbose_name_plural = "Bölümler"
    
    def __str__(self):
        return self.name

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Ders Adı", max_length=100)
    department = models.ManyToManyField(Department)

    class Meta:
        verbose_name = "Ders"
        verbose_name_plural = "Dersler"

    def __str__(self):
        return self.name

class Outhor(models.Model):
    genders = (
        ('M', 'Erkek'),
        ('F', 'Kadin'),
    )

    title_tpyes = (
        ('1','Profesör'),
        ('2','Doçent'),
        ('3','Doktor'),
        ('4','Öğretim Görevlisi'),
        ('5','Araştirma Görevlisi'),
        ('6','Öğretmen'),
        ('7','Yazar'),
        ('8','Araştirmaci'),
        ('9','Üye'),
    )

    id = models.AutoField(primary_key=True)
    first_name = models.CharField("Adı", max_length=100)
    last_name = models.CharField("Soyadı", max_length=100)
    biography = models.TextField("Özgeçmiş", max_length=3000, null=True, blank=True)
    image_name = models.CharField("Profil Resmi", max_length=200, null=True, blank=True)
    date_of_birth = models.DateField("Doğum Tarihi", null=True, blank=True)
    gender = models.CharField("Cinsiyet", max_length=1, choices=genders)
    title_type = models.CharField("Ünvan", max_length=1, choices=title_tpyes)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}" 
    
    full_name.fget.short_description = "Ad Soyad"

    class Meta:
        verbose_name = "Yazar"
        verbose_name_plural = "Yazarlar"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.title_tpyes[int(self.title_type)-1][1]})"
  
class File(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("Başlık", max_length=250)
    description = RichTextField("Açıklama", null=True, blank=True)
    file_name = models.ImageField("Dosya Adı", upload_to="Drive")
    file_cover = models.ImageField("Dosya Resmi", upload_to="Drive")
    upload_date = models.DateTimeField(auto_now=True)
    date = models.DateField("Yüklenme Tarihi", null=True, blank=True)
    slug = models.SlugField(unique=True,db_index=True)
    language = models.CharField("Dil", max_length=100)
    outhor = models.ForeignKey(Outhor,on_delete=models.SET_NULL, null=True,blank=True)
    scholl = models.ForeignKey(Scholl, models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=0)
    is_home = models.BooleanField(default=0)

    class Meta:
        verbose_name = "Dosya"
        verbose_name_plural = "Dosyalar"

    def __str__(self):
        return self.title

class Slider(models.Model):
        id = models.AutoField(primary_key=True)
        title = models.CharField(max_length=200)
        image = models.ImageField(upload_to="files")
        file = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True)
        is_active = models.BooleanField(default=False)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField("Kullanıcı Adı", max_length=30)
    email = models.EmailField("E-Posta", default="")
    text = models.TextField("Yorum", max_length=500)
    rating = models.IntegerField("Oy", null=True)
    date_added = models.DateTimeField("Yorum Tarihi", auto_now=True, null=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"