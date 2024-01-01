from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class OCRDocument(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True,null=True, blank=True)
    title = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    ocr_text = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='documents/',null=True, blank=True)  # Örnek bir yükleme dizini belirtildi

    def __str__(self):
        return self.title
