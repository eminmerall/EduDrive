from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.fields import CharField


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    adress = models.CharField(max_length=400)
    email = models.EmailField(null=True, blank=True)
    phone1 = models.CharField(max_length=20,null=True, blank=True)
    phone2 = models.CharField(max_length=20,null=True, blank=True)

class Scholl(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True, blank=True)

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    scholl = models.ManyToManyField(Scholl)

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ManyToManyField(Department)

class Owner(models.Model):
    genders = (
        ('M', 'Erkek'),
        ('F', 'Kadın'),
    )

    title_tpyes = (
        ('1','Profesör'),
        ('2','Doçent'),
        ('3','Doktor'),
        ('4','Öğretim Görevlisi'),
        ('5','Araştırma Görevlisi'),
        ('6','Öğretmen'),
        ('7','Yazar'),
        ('8','Araştırmacı'),
        ('9','Üye')
    )

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.CharField(max_length=3000, null=True, blank=True)
    image_name = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=genders,null=True, blank=True)
    title_type = models.CharField(max_length=1, choices=title_tpyes,null=True, blank=True)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True, blank=True)

    
class File(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.TextField(validators= [MinLengthValidator(15)], null=True, blank=True)
    file_name = models.CharField(max_length=200)
    file_cover = models.CharField(max_length=200,null=True, blank=True)
    upload_date = models.DateTimeField(auto_now=True)
    date = models.DateField(null=True, blank=True,null=True, blank=True)
    slug = models.SlugField(unique=True,db_index=True)
    language = models.CharField(max_length=100)
    owner = models.ManyToManyField(Owner, null=True, blank=True)
    lesson = models.ManyToManyField(Lesson, null=True, blank=True)
