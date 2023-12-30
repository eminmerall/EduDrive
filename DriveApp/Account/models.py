from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from Drive.models import Contact, Department, Scholl


# Create your models here.

class Profile(models.Model):
    genders = (
         ('M', 'Erkek'),
         ('F', 'Kadın'),
     )
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to="Account", blank=True)
    date_of_birth = models.DateField("Doğum Tarihi", null=True, blank=True)
    gender = models.CharField("Cinsiyet", max_length=1, choices=genders,null=True, blank=True)
    scholl = models.ForeignKey(Scholl, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()