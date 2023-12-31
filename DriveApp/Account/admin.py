from django.contrib import admin

from Account.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'scholl','department',)
    search_fields = ('first_name', 'last_name',)

admin.site.register(Profile, ProfileAdmin)
