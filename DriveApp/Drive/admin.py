from django.contrib import admin

from Drive.models import Contact, Scholl, Department, Lesson, User, Outhor, File, Comment

# Register your models here.

class FileAdmin(admin.ModelAdmin):
    list_display = ('title','is_active','is_home')
    prepopulated_fields = {'slug': ('title',) }
    list_filter  = ('department','language','is_active','is_home')
    search_fields = ('title', 'description')

class OuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender','title_type')
    list_filter = ('title_type',)
    search_fields = ('first_name', 'last_name')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('username','file',)
    list_filter = ('username','file',)
    search_fields =('file__title','text')


admin.site.register(Contact)
admin.site.register(Scholl)
admin.site.register(Department)
admin.site.register(Lesson)
admin.site.register(User)
admin.site.register(Outhor, OuthorAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Comment, CommentAdmin)
 